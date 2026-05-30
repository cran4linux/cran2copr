%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  greenR
%global packver   0.0.1.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1.7
Release:          1%{?dist}%{?buildtag}
Summary:          Green Index Quantification, Analysis and Visualization

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-arrow 
BuildRequires:    R-CRAN-classInt 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-duckdb 
BuildRequires:    R-CRAN-elevatr 
BuildRequires:    R-CRAN-exactextractr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggspatial 
BuildRequires:    R-CRAN-h3jsr 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-ineq 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-leaflet 
BuildRequires:    R-CRAN-leaflet.extras 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-maptiles 
BuildRequires:    R-CRAN-moments 
BuildRequires:    R-CRAN-OpenImageR 
BuildRequires:    R-CRAN-osmdata 
BuildRequires:    R-CRAN-osrm 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-rstac 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-sfnetworks 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-spatstat.geom 
BuildRequires:    R-CRAN-spdep 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-SuperpixelImageSegmentation 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyterra 
BuildRequires:    R-CRAN-units 
BuildRequires:    R-CRAN-viridisLite 
Requires:         R-CRAN-arrow 
Requires:         R-CRAN-classInt 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-duckdb 
Requires:         R-CRAN-elevatr 
Requires:         R-CRAN-exactextractr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggspatial 
Requires:         R-CRAN-h3jsr 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-ineq 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-leaflet 
Requires:         R-CRAN-leaflet.extras 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-maptiles 
Requires:         R-CRAN-moments 
Requires:         R-CRAN-OpenImageR 
Requires:         R-CRAN-osmdata 
Requires:         R-CRAN-osrm 
Requires:         R-parallel 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-rstac 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-sfnetworks 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-spatstat.geom 
Requires:         R-CRAN-spdep 
Requires:         R-stats 
Requires:         R-CRAN-SuperpixelImageSegmentation 
Requires:         R-CRAN-terra 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyterra 
Requires:         R-CRAN-units 
Requires:         R-CRAN-viridisLite 

%description
Quantification, analysis, and visualization of urban greenness within city
networks using data from 'OpenStreetMap' <https://www.openstreetmap.org>.

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
