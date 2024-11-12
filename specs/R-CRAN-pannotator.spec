%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pannotator
%global packver   1.0.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0.4
Release:          1%{?dist}%{?buildtag}
Summary:          Visualisation and Annotation of 360 Degree Imagery

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-bslib 
BuildRequires:    R-CRAN-colourpicker 
BuildRequires:    R-CRAN-config 
BuildRequires:    R-CRAN-configr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-exiftoolr 
BuildRequires:    R-CRAN-geojsonsf 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-golem 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-jpeg 
BuildRequires:    R-CRAN-jsonify 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-leaflet 
BuildRequires:    R-CRAN-leaflet.extras 
BuildRequires:    R-CRAN-leafpm 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinyFiles 
BuildRequires:    R-CRAN-shinyhelper 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-shinythemes 
BuildRequires:    R-CRAN-shinyWidgets 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-bslib 
Requires:         R-CRAN-colourpicker 
Requires:         R-CRAN-config 
Requires:         R-CRAN-configr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-exiftoolr 
Requires:         R-CRAN-geojsonsf 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-golem 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-jpeg 
Requires:         R-CRAN-jsonify 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-leaflet 
Requires:         R-CRAN-leaflet.extras 
Requires:         R-CRAN-leafpm 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinyFiles 
Requires:         R-CRAN-shinyhelper 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-shinythemes 
Requires:         R-CRAN-shinyWidgets 
Requires:         R-CRAN-stringr 
Requires:         R-tools 
Requires:         R-utils 

%description
Provides a customisable R 'shiny' app for immersively visualising, mapping
and annotating panospheric (360 degree) imagery. The flexible interface
allows annotation of any geocoded images using up to 4 user specified
dropdown menus. The app uses 'leaflet' to render maps that display the
geo-locations of images and panellum <https://pannellum.org/>, a
lightweight panorama viewer for the web, to render images in virtual 360
degree viewing mode. Key functions include the ability to draw on & export
parts of 360 images for downstream applications. Users can also draw
polygons and points on map imagery related to the panoramic images and
export them for further analysis. Downstream applications include using
annotations to train Artificial Intelligence/Machine Learning (AI/ML)
models and geospatial modelling and analysis of camera based survey data.

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
