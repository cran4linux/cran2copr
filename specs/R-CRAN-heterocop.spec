%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  heterocop
%global packver   0.1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Semi-Parametric Estimation with Gaussian Copula

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-doSNOW 
BuildRequires:    R-utils 
Requires:         R-CRAN-mvtnorm 
Requires:         R-stats 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-matrixcalc 
Requires:         R-graphics 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-doSNOW 
Requires:         R-utils 

%description
A method for generating random vectors which are linked by a Gaussian
copula. It also enables to estimate the correlation matrix of the Gaussian
copula in order to identify independencies within the data.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
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
