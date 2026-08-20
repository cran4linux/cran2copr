%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  compIndexBuilder
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Composite Index Builder & Analytics 'shiny' App

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinydashboard 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-networkD3 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-corrplot 
BuildRequires:    R-CRAN-missForest 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-jsonlite 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinydashboard 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-networkD3 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-corrplot 
Requires:         R-CRAN-missForest 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-jsonlite 

%description
Provides an interactive 'shiny' application for constructing, analysing,
comparing, and visualising composite indices from tabular multidimensional
data. Supports multi-sheet 'Excel' workbooks with active-sheet selection,
refresh controls, per-sheet and workbook-wide exports, missing-data
processing, indicator direction and normalisation controls, equal and
custom weighting, entity-level ranking, time-series analysis and
forecasting, entity comparisons, pillar-based sub-indices with equal,
custom, correlation-based, or principal-component weights, and diagnostic
tools including internal-consistency reliability assessment, coefficient
of variation, principal component analysis, sensitivity analysis,
correlation heatmaps, and weighted flow visualizations.

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
