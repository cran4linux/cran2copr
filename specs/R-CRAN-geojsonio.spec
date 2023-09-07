%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  geojsonio
%global packver   0.11.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.11.3
Release:          1%{?dist}%{?buildtag}
Summary:          Convert Data from and to 'GeoJSON' or 'TopoJSON'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite >= 0.9.21
BuildRequires:    R-CRAN-sf >= 0.6
BuildRequires:    R-CRAN-readr >= 0.2.2
BuildRequires:    R-CRAN-geojson >= 0.2.0
BuildRequires:    R-CRAN-crul 
BuildRequires:    R-CRAN-geojsonsf 
BuildRequires:    R-CRAN-jqr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-V8 
Requires:         R-CRAN-jsonlite >= 0.9.21
Requires:         R-CRAN-sf >= 0.6
Requires:         R-CRAN-readr >= 0.2.2
Requires:         R-CRAN-geojson >= 0.2.0
Requires:         R-CRAN-crul 
Requires:         R-CRAN-geojsonsf 
Requires:         R-CRAN-jqr 
Requires:         R-CRAN-magrittr 
Requires:         R-methods 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-V8 

%description
Convert data to 'GeoJSON' or 'TopoJSON' from various R classes, including
vectors, lists, data frames, shape files, and spatial classes.
'geojsonio' does not aim to replace packages like 'sp', 'rgdal', 'rgeos',
but rather aims to be a high level client to simplify conversions of data
from and to 'GeoJSON' and 'TopoJSON'.

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
