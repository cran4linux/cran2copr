%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  greenR
%global packver   0.0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Green Index Quantification, Analysis and Visualization

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-osmdata 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-leaflet 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-SuperpixelImageSegmentation 
BuildRequires:    R-CRAN-OpenImageR 
BuildRequires:    R-CRAN-osrm 
BuildRequires:    R-CRAN-spatstat.geom 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-units 
BuildRequires:    R-CRAN-duckdb 
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-viridisLite 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-jsonlite 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-osmdata 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-leaflet 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-SuperpixelImageSegmentation 
Requires:         R-CRAN-OpenImageR 
Requires:         R-CRAN-osrm 
Requires:         R-CRAN-spatstat.geom 
Requires:         R-stats 
Requires:         R-CRAN-units 
Requires:         R-CRAN-duckdb 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-viridisLite 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-jsonlite 

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
