%global __brp_check_rpaths %{nil}
%global packname  MDMAPR
%global packver   0.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.3
Release:          1%{?dist}%{?buildtag}
Summary:          Molecular Detection Mapping and Analysis Platform

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-RMySQL 
BuildRequires:    R-CRAN-shinydashboard 
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-leaflet 
BuildRequires:    R-CRAN-leaflet.extras 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-reactable 
BuildRequires:    R-CRAN-writexl 
BuildRequires:    R-CRAN-xfun 
BuildRequires:    R-CRAN-berryFunctions 
BuildRequires:    R-CRAN-shinyWidgets 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-bslib 
BuildRequires:    R-CRAN-htmlwidgets 
Requires:         R-CRAN-RMySQL 
Requires:         R-CRAN-shinydashboard 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-leaflet 
Requires:         R-CRAN-leaflet.extras 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-reactable 
Requires:         R-CRAN-writexl 
Requires:         R-CRAN-xfun 
Requires:         R-CRAN-berryFunctions 
Requires:         R-CRAN-shinyWidgets 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-htmltools 
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-CRAN-bslib 
Requires:         R-CRAN-htmlwidgets 

%description
Runs a Shiny web application that merges raw 'qPCR' fluorescence data with
related metadata to visualize species presence/absence detection patterns
and assess data quality. The application calculates threshold values from
raw fluorescence data using a method based on the second derivative
method, Luu-The et al (2005) <doi:10.2144/05382RR05>, and utilizes the
‘chipPCR’ package by Rödiger, Burdukiewicz, & Schierack (2015)
<doi:10.1093/bioinformatics/btv205> to calculate Cq values. The
application has the ability to connect to a custom developed MySQL
database to populate the applications interface. The application allows
users to interact with visualizations such as a dynamic map, amplification
curves and standard curves, that allow for zooming and/or filtering. It
also enables the generation of customized exportable reports based on
filtered mapping data.

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
