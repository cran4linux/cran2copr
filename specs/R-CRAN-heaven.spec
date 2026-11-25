%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  heaven
%global packver   2026.11.24
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2026.11.24
Release:          1%{?dist}%{?buildtag}
Summary:          Fast Data Preparation for Danish Registry Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-data.table >= 1.9.6
BuildRequires:    R-CRAN-Rcpp >= 1.0.14
BuildRequires:    R-stats 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-lava 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-data.table >= 1.9.6
Requires:         R-CRAN-Rcpp >= 1.0.14
Requires:         R-stats 
Requires:         R-parallel 
Requires:         R-CRAN-foreach 
Requires:         R-utils 
Requires:         R-CRAN-lava 
Requires:         R-CRAN-lubridate 
Requires:         R-tools 

%description
Prepares and analyses large Danish administrative and health registry
datasets. Provides memory-efficient routines for cohort construction, time
splitting, code-based condition identification, prescription exposure
periods, risk-set matching, and direct standardisation. The package is
designed for secure research environments such as Statistics Denmark and
builds on the data structures provided by the 'data.table' package.

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
