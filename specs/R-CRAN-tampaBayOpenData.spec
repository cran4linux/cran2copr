%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tampaBayOpenData
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          An R Interface to Tampa Bay Public Open Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble >= 3.0.0
BuildRequires:    R-CRAN-jsonlite >= 1.6.0
BuildRequires:    R-CRAN-httr2 >= 1.2.3
Requires:         R-CRAN-tibble >= 3.0.0
Requires:         R-CRAN-jsonlite >= 1.6.0
Requires:         R-CRAN-httr2 >= 1.2.3

%description
Provides a lightweight R interface for discovering and retrieving public
'ArcGIS' datasets across the Tampa Bay region. Search civic datasets and
load records directly into R without manually navigating separate portals,
constructing REST API requests, or handling pagination. Supports public
data published by the City of Tampa, City of St. Petersburg, City of
Clearwater, Hillsborough County, Pinellas County, and Tampa Bay Regional
Planning Council. Discover layers in these and other public 'ArcGIS'
portals and retrieve them by their REST URLs. A publisher registry
configures discovery, while a separate dataset registry identifies layers
checked by package maintainers. Filter catalogs by source, geometry,
topic, category, and modification date. Retrieve queryable layers with
validated pagination, bounded previews, server-side filtering, typed
tabular results, optional spatial objects, and source provenance. Save
large downloads as local chunks that can be validated and resumed.
Designed for analysts, researchers, students, journalists, and civic
technologists who work across separate public data portals. Public source
pages are the City of Tampa GeoHub
<https://city-tampa.opendata.arcgis.com/>, St. Petersburg ArcGIS portal
<https://csp.maps.arcgis.com/home/index.html>, Clearwater ArcGIS portal
<https://cityofclearwater.maps.arcgis.com/home/index.html>, Hillsborough
County GeoHub
<https://hcfl.gov/about-hillsborough/open-data-and-gis/geohub>, Pinellas
County Enterprise GIS <https://new-pinellas-egis.opendata.arcgis.com/>,
and Tampa Bay Regional Planning Council GeoHub
<https://opendata-tbrpc.hub.arcgis.com/>.

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
