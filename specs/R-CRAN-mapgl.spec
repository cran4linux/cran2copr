%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mapgl
%global packver   0.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.1
Release:          1%{?dist}%{?buildtag}
Summary:          Interactive Maps with 'Mapbox GL JS' and 'MapLibre GL JS'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-geojsonsf 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-CRAN-classInt 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-viridisLite 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-geojsonsf 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-htmltools 
Requires:         R-grDevices 
Requires:         R-CRAN-base64enc 
Requires:         R-CRAN-terra 
Requires:         R-CRAN-classInt 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-viridisLite 

%description
Provides an interface to the 'Mapbox GL JS'
(<https://docs.mapbox.com/mapbox-gl-js/guides>) and the 'MapLibre GL JS'
(<https://maplibre.org/maplibre-gl-js/docs/>) interactive mapping
libraries to help users create custom interactive maps in R.  Users can
create interactive globe visualizations; layer 'sf' objects to create
filled maps, circle maps, 'heatmaps', and three-dimensional graphics; and
customize map styles and views.  The package also includes utilities to
use 'Mapbox' and 'MapLibre' maps in 'Shiny' web applications.

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
