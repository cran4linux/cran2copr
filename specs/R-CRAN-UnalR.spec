%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  UnalR
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Una implementación de funciones de uso interno

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-plotly >= 4.11.0
BuildRequires:    R-CRAN-ggplot2 >= 4.0.0
BuildRequires:    R-CRAN-treemap >= 2.4.4
BuildRequires:    R-CRAN-leaflet >= 2.2.3
BuildRequires:    R-CRAN-sunburstR >= 2.1.8
BuildRequires:    R-CRAN-tidyr >= 1.3.1
BuildRequires:    R-CRAN-rlang >= 1.1.6
BuildRequires:    R-CRAN-dplyr >= 1.1.4
BuildRequires:    R-CRAN-dygraphs >= 1.1.1.6
BuildRequires:    R-CRAN-d3r >= 1.1.0
BuildRequires:    R-CRAN-forcats >= 1.0.0
BuildRequires:    R-CRAN-gt >= 1.0.0
BuildRequires:    R-CRAN-leaflet.extras >= 1.0.0
BuildRequires:    R-CRAN-highcharter >= 0.9.4
BuildRequires:    R-CRAN-fmsb >= 0.7.6
BuildRequires:    R-CRAN-echarts4r >= 0.4.6
BuildRequires:    R-CRAN-DT >= 0.34.0
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-data.tree 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-ggspatial 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-gridSVG 
BuildRequires:    R-CRAN-gtExtras 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-maps 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-png 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-webshot 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-CRAN-zoo 
Requires:         R-CRAN-plotly >= 4.11.0
Requires:         R-CRAN-ggplot2 >= 4.0.0
Requires:         R-CRAN-treemap >= 2.4.4
Requires:         R-CRAN-leaflet >= 2.2.3
Requires:         R-CRAN-sunburstR >= 2.1.8
Requires:         R-CRAN-tidyr >= 1.3.1
Requires:         R-CRAN-rlang >= 1.1.6
Requires:         R-CRAN-dplyr >= 1.1.4
Requires:         R-CRAN-dygraphs >= 1.1.1.6
Requires:         R-CRAN-d3r >= 1.1.0
Requires:         R-CRAN-forcats >= 1.0.0
Requires:         R-CRAN-gt >= 1.0.0
Requires:         R-CRAN-leaflet.extras >= 1.0.0
Requires:         R-CRAN-highcharter >= 0.9.4
Requires:         R-CRAN-fmsb >= 0.7.6
Requires:         R-CRAN-echarts4r >= 0.4.6
Requires:         R-CRAN-DT >= 0.34.0
Requires:         R-CRAN-cli 
Requires:         R-CRAN-data.tree 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-ggspatial 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-grid 
Requires:         R-CRAN-gridSVG 
Requires:         R-CRAN-gtExtras 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-maps 
Requires:         R-methods 
Requires:         R-CRAN-png 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-sp 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-utils 
Requires:         R-CRAN-webshot 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-xts 
Requires:         R-CRAN-zoo 

%description
Una herramienta rápida y consistente para la disposición de microdatos y
la visualización de las cifras y estadísticas oficiales de la Universidad
Nacional de Colombia <https://unal.edu.co>. Contiene una biblioteca de
funciones gráficas, tanto estáticas como interactivas, que ofrece
numerosos tipos de gráficos con una sintaxis altamente configurable y
simple. Entre estos encontramos la visualización de tablas HTML, series,
gráficos de barras y circulares, mapas, etc. Todo lo anterior apoyado en
bibliotecas de JavaScript. English: A fast and consistent tool for the
arrangement of microdata and the visualization of official figures and
statistics from the National University of Colombia <https://unal.edu.co>.
It includes a library of graphical functions, both static and interactive,
offering numerous types of charts with a highly configurable and simple
syntax. Among these, we find the visualization of HTML tables, series, bar
and pie charts, maps, etc. It provides the capability to transition from
the interactive to the dynamic world and from one library to another
without changing function or syntax.

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
