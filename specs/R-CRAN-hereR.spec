%global __brp_check_rpaths %{nil}
%global packname  hereR
%global packver   0.7.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.0
Release:          1%{?dist}%{?buildtag}
Summary:          'sf'-Based Interface to the 'HERE' REST APIs

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-curl >= 4.3
BuildRequires:    R-CRAN-jsonlite >= 1.7.0
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-data.table >= 1.13.0
BuildRequires:    R-CRAN-crul >= 1.1.0
BuildRequires:    R-CRAN-sf >= 0.9.0
BuildRequires:    R-CRAN-flexpolyline >= 0.2.0
Requires:         R-CRAN-curl >= 4.3
Requires:         R-CRAN-jsonlite >= 1.7.0
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-data.table >= 1.13.0
Requires:         R-CRAN-crul >= 1.1.0
Requires:         R-CRAN-sf >= 0.9.0
Requires:         R-CRAN-flexpolyline >= 0.2.0

%description
Interface to the 'HERE' REST APIs
<https://developer.here.com/develop/rest-apis>: (1) geocode and
autosuggest addresses or reverse geocode POIs using the 'Geocoder' API;
(2) route directions, travel distance or time matrices and isolines using
the 'Routing', 'Matrix Routing' and 'Isoline Routing' APIs; (3) request
real-time traffic flow and incident information from the 'Traffic' API;
(4) find request public transport connections and nearby stations from the
'Public Transit' API; (5) request intermodal routes using the 'Intermodal
Routing' API; (6) get weather forecasts, reports on current weather
conditions, astronomical information and alerts at a specific location
from the 'Destination Weather' API. Locations, routes and isolines are
returned as 'sf' objects.

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
