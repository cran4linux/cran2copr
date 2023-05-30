%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  meteoland
%global packver   2.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Landscape Meteorology Tools

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-stars 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-units 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-ncdfgeom 
BuildRequires:    R-CRAN-ncmeta 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-cubelyr 
Requires:         R-methods 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-stars 
Requires:         R-stats 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-units 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-ncdfgeom 
Requires:         R-CRAN-ncmeta 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-cubelyr 

%description
Functions to estimate weather variables at any position of a landscape [De
Caceres et al. (2018) <doi:10.1016/j.envsoft.2018.08.003>].

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
