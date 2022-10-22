%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  csodata
%global packver   1.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Download Data from the CSO 'PxStat' API

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-rjstat 
BuildRequires:    R-CRAN-R.cache 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-lubridate 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-rjstat 
Requires:         R-CRAN-R.cache 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-lubridate 

%description
Imports 'PxStat' data in JSON-stat format and (optionally) reshapes it
into wide format. The Central Statistics Office (CSO) is the national
statistical institute of Ireland and 'PxStat' is the CSOs online database
of Official Statistics. This database contains current and historical data
series compiled from CSO statistical releases and is accessed at
<http://data.cso.ie>. The CSO 'PxStat' Application Programming Interface
(API), which is accessed in this package, provides access to 'PxStat' data
in JSON-stat format at <http://data.cso.ie>. This dissemination tool
allows developers machine to machine access to CSO 'PxStat' data.

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
