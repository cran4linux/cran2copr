%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  azuremapsr
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Interface to the 'Azure Maps' API

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-geojsonsf >= 2.0.3
BuildRequires:    R-CRAN-jsonlite >= 2.0.0
BuildRequires:    R-CRAN-lubridate >= 1.9.4
BuildRequires:    R-CRAN-stringr >= 1.5.1
BuildRequires:    R-CRAN-httr2 >= 1.2.1
BuildRequires:    R-CRAN-purrr >= 1.1.0
BuildRequires:    R-CRAN-sf >= 1.0.21
BuildRequires:    R-CRAN-rlist >= 0.4.6.2
Requires:         R-CRAN-geojsonsf >= 2.0.3
Requires:         R-CRAN-jsonlite >= 2.0.0
Requires:         R-CRAN-lubridate >= 1.9.4
Requires:         R-CRAN-stringr >= 1.5.1
Requires:         R-CRAN-httr2 >= 1.2.1
Requires:         R-CRAN-purrr >= 1.1.0
Requires:         R-CRAN-sf >= 1.0.21
Requires:         R-CRAN-rlist >= 0.4.6.2

%description
Provides a wrapper for the Microsoft 'Azure Maps' REST APIs
<https://learn.microsoft.com/en-us/rest/api/maps/route?view=rest-maps-2025-01-01>,
enabling users to access mapping and geospatial services directly from R.
This package simplifies authenticating, building, and sending requests for
services like route directions. It handles conversions between R objects
(such as 'sf' objects) and the GeoJSON+JSON format required by the API,
making it easier to integrate 'Azure Maps' into R-based data analysis
workflows.

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
