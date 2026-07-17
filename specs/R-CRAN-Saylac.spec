%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Saylac
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Spatial Analysis of Yearly, Longitudinal, and Areal Change

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-bs4Dash 
BuildRequires:    R-CRAN-classInt 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-maps 
BuildRequires:    R-CRAN-Metrics 
BuildRequires:    R-CRAN-nnfor 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-rnaturalearth 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-spdep 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tidyverse 
BuildRequires:    R-CRAN-trend 
BuildRequires:    R-CRAN-tseries 
BuildRequires:    R-CRAN-zoo 
Requires:         R-CRAN-bs4Dash 
Requires:         R-CRAN-classInt 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-maps 
Requires:         R-CRAN-Metrics 
Requires:         R-CRAN-nnfor 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-rnaturalearth 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-spdep 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tidyverse 
Requires:         R-CRAN-trend 
Requires:         R-CRAN-tseries 
Requires:         R-CRAN-zoo 

%description
Provides the Saylac Shiny application for multidisciplinary analysis of
global, national, and regional indicators observed across places and
years. SAYLAC abbreviates Spatial Analysis of Yearly, Longitudinal, and
Areal Change. The platform supports spatial diagnostics, longitudinal data
exploration, time-series diagnostics, comparative forecasting, and
automated reporting for development, health, education, economic,
environmental, and social indicators. The application implements three
connected modules: Spatial Analysis Workflow for exploratory spatial data
analysis, Single Model Diagnostics for stationarity testing, trend
diagnostics, and comparative forecasting, and Spatial Uncertainty and
Reporting Analysis Dashboard for forecast mapping, spatial clustering, and
reporting. The application supports choropleth mapping, Moran's I, Geary's
C, Local Indicators of Spatial Association, Getis-Ord Gi star statistics,
spatial correlograms, Theil-Sen trend estimation, Mann-Kendall testing,
Autoregressive Integrated Moving Average models, Exponential Smoothing
State Space models, neural network autoregression, BATS, TBATS, theta
forecasting, symmetric mean absolute percentage error model comparison,
and report generation. The platform was first applied in Touryare and
Mohamud (2026) <doi:10.1007/s43621-026-04022-x> for integrated
spatial-temporal forecasting of educational attainment in Eastern Africa
toward Sustainable Development Goal 4.

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
