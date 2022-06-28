%global __brp_check_rpaths %{nil}
%global packname  mapboxapi
%global packver   0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4
Release:          1%{?dist}%{?buildtag}
Summary:          R Interface to 'Mapbox' Web Services

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-tidyr >= 1.0.0
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-aws.s3 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-slippymath 
BuildRequires:    R-CRAN-protolite 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-geojsonsf 
BuildRequires:    R-CRAN-magick 
BuildRequires:    R-CRAN-leaflet 
BuildRequires:    R-CRAN-units 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-png 
BuildRequires:    R-CRAN-jpeg 
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-tidyr >= 1.0.0
Requires:         R-CRAN-httr 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-aws.s3 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-slippymath 
Requires:         R-CRAN-protolite 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-geojsonsf 
Requires:         R-CRAN-magick 
Requires:         R-CRAN-leaflet 
Requires:         R-CRAN-units 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-png 
Requires:         R-CRAN-jpeg 

%description
Includes support for 'Mapbox' Navigation APIs, including directions,
isochrones, and route optimization; the Search API for forward and reverse
geocoding; the Maps API for interacting with 'Mapbox' vector tilesets and
visualizing 'Mapbox' maps in R; and the 'tippecanoe' tile-generation
utility. See <https://docs.mapbox.com/api/> for more information about the
'Mapbox' APIs.

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
