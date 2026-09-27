%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mappingAS
%global packver   1.13.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.13.2
Release:          1%{?dist}%{?buildtag}
Summary:          Spatial Metrics and Habitat Conversion for Extinction Risk Assessment

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-terra >= 1.7.0
BuildRequires:    R-CRAN-sf >= 1.0.0
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-bslib 
BuildRequires:    R-CRAN-leaflet 
BuildRequires:    R-CRAN-units 
BuildRequires:    R-CRAN-lwgeom 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-grid 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-officer 
Requires:         R-CRAN-terra >= 1.7.0
Requires:         R-CRAN-sf >= 1.0.0
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-bslib 
Requires:         R-CRAN-leaflet 
Requires:         R-CRAN-units 
Requires:         R-CRAN-lwgeom 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-rlang 
Requires:         R-grid 
Requires:         R-tools 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-officer 

%description
A spatial analytical framework for preliminary species extinction-risk
screening following the IUCN Red List Criterion B guidelines. From
occurrence points it computes the Extent of Occurrence (EOO) and Area of
Occupancy (AOO) on a data-centred equal-area projection, assigns
provisional Criterion B categories, and integrates 'MapBiomas'
land-use/land-cover data to quantify the proportion of anthropogenic
conversion versus remaining natural habitat within each range metric, with
per-class breakdowns and land-cover time series. Several 'MapBiomas'
initiatives are supported through one standardised legend - 'MapBiomas'
Brazil, the Pan-Amazon / Amazonia collection (RAISG), Colombia, Argentina,
Bolivia, Chile, Ecuador, Peru, Venezuela, Paraguay and Uruguay - so a
species anywhere these products cover can be screened as readily as a
Brazilian one. For ranges outside 'MapBiomas' coverage it can fall back to
the global 'Esri' / 'Impact Observatory' 10 m annual land cover derived
from 'Sentinel-2' (the product behind the 'ArcGIS' Living Atlas Land Cover
Explorer), so a species anywhere on Earth can be screened. It also
integrates 'MapBiomas' Fire to compute burned-area metrics and fire time
series, and quantifies the overlap of the range with protected areas from
the global World Database on Protected Areas (WDPA). 'MapBiomas' data are
read either locally over the network via 'GDAL' '/vsicurl/' (no 'Google
Earth Engine' account required) or server-side through 'Google Earth
Engine' (GEE) for large-scale assessments. Outputs include interactive and
publication ready maps and charts, spatial (shapefile/'GeoPackage') and
raster exports, and a written assessment report (HTML, text or Word). An
interactive 'shiny' application ties the whole workflow together for
reproducible conservation planning.

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
