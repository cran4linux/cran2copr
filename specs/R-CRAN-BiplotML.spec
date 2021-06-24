%global __brp_check_rpaths %{nil}
%global packname  BiplotML
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Biplots Estimation with Algorithms ML

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-optimr 
BuildRequires:    R-CRAN-optimx 
BuildRequires:    R-CRAN-shapes 
Requires:         R-CRAN-optimr 
Requires:         R-CRAN-optimx 
Requires:         R-CRAN-shapes 

%description
Logistic Biplot is a method that allows representing multivariate binary
data on a subspace of low dimension, where each individual is represented
by a point and each variable as vectors directed through the origin. The
orthogonal projection of individuals onto these vectors predicts the
expected probability that the characteristic occurs. The package contains
new techniques to estimate the model parameters and constructs in each
case the 'Logistic-Biplot'. References can be found in the help of each
procedure.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
