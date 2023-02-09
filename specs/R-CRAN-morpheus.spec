%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  morpheus
%global packver   1.0-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Estimate Parameters of Mixtures of Logistic Regressions

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-jointDiag 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-pracma 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-jointDiag 
Requires:         R-methods 
Requires:         R-CRAN-pracma 

%description
Mixture of logistic regressions parameters (H)estimation with (U)spectral
methods. The main methods take d-dimensional inputs and a vector of binary
outputs, and return parameters according to the GLMs mixture model
(General Linear Model). For more details see chapter 3 in the PhD thesis
of Mor-Absa Loum: <https://www.theses.fr/s156435>, available here
<https://theses.hal.science/tel-01877796/document>.

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
