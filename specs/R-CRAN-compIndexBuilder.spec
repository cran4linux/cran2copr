%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  compIndexBuilder
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Composite Index Builder & Analytics 'shiny' App

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-shinydashboard 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-corrplot 
BuildRequires:    R-CRAN-missForest 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-networkD3 
BuildRequires:    R-CRAN-psych 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-shinydashboard 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-corrplot 
Requires:         R-CRAN-missForest 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-networkD3 
Requires:         R-CRAN-psych 

%description
Provides an interactive 'shiny' web application for constructing,
analyzing, and visualizing composite indices from multidimensional
datasets. Users can upload or select indicator data, group variables into
logical categories, apply normalization and weighting methods (such as
'equal' or 'custom' schemes), and compute aggregate composite indices. The
'shiny' interface includes tools for exploring results through tables,
plots, and data exports, making it useful for researchers, policymakers,
and analysts interested in index-based evaluations.

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
