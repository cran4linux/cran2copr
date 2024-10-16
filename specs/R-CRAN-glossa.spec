%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  glossa
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          User-Friendly 'shiny' App for Bayesian Species Distribution Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-bs4Dash 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-dbarts 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-GeoThinneR 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-leaflet 
BuildRequires:    R-CRAN-markdown 
BuildRequires:    R-CRAN-mcp 
BuildRequires:    R-CRAN-pROC 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-shinyWidgets 
BuildRequires:    R-CRAN-sparkline 
BuildRequires:    R-CRAN-svglite 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-CRAN-tidyterra 
BuildRequires:    R-CRAN-waiter 
BuildRequires:    R-CRAN-zip 
Requires:         R-CRAN-bs4Dash 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-dbarts 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-GeoThinneR 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-leaflet 
Requires:         R-CRAN-markdown 
Requires:         R-CRAN-mcp 
Requires:         R-CRAN-pROC 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-shinyWidgets 
Requires:         R-CRAN-sparkline 
Requires:         R-CRAN-svglite 
Requires:         R-CRAN-terra 
Requires:         R-CRAN-tidyterra 
Requires:         R-CRAN-waiter 
Requires:         R-CRAN-zip 

%description
A user-friendly 'shiny' application for Bayesian machine learning analysis
of marine species distributions. GLOSSA (Global Species Spatiotemporal
Analysis) uses Bayesian Additive Regression Trees (BART; Chipman, George,
and McCulloch (2010) <doi:10.1214/09-AOAS285>) to model species
distributions with intuitive workflows for data upload, processing, model
fitting, and result visualization. It supports presence-absence and
presence-only data (with pseudo-absence generation), spatial thinning,
cross-validation, and scenario-based projections. GLOSSA is designed to
facilitate ecological research by providing easy-to-use tools for
analyzing and visualizing marine species distributions across different
spatial and temporal scales.

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
