%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  lfl
%global packver   2.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Linguistic Fuzzy Logic

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildRequires:    R-CRAN-forecast >= 5.5
BuildRequires:    R-CRAN-Rcpp >= 0.12.12
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-tseries 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-forecast >= 5.5
Requires:         R-CRAN-Rcpp >= 0.12.12
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-tseries 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-tibble 

%description
Various algorithms related to linguistic fuzzy logic: mining for
linguistic fuzzy association rules, composition of fuzzy relations,
performing perception-based logical deduction (PbLD), and forecasting
time-series using fuzzy rule-based ensemble (FRBE). The package also
contains basic fuzzy-related algebraic functions capable of handling
missing values in different styles (Bochvar, Sobocinski, Kleene etc.),
computation of Sugeno integrals and fuzzy transform.

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
