%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  archeoViz
%global packver   1.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Visualisation, Exploration, and Web Communication of Archaeological Spatial Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-geometry 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-svglite 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinythemes 
BuildRequires:    R-CRAN-knitr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-geometry 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-svglite 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinythemes 
Requires:         R-CRAN-knitr 

%description
An R 'Shiny' application for visual and statistical exploration and web
communication of archaeological spatial data, either remains or sites. It
offers interactive 3D and 2D visualisations (cross sections and maps of
remains, timeline of the work made in a site) which can be exported in SVG
and HTML formats. It performs simple spatial statistics (convex hull,
regression surfaces, 2D kernel density estimation) and allows exporting
data to other online applications for more complex methods. 'archeoViz'
can be used offline locally or deployed on a server, either with
interactive input of data or with a static data set. Example is provided
at <https://analytics.huma-num.fr/archeoviz/en>.

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
