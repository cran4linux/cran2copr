%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MVPapp
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Interactive Platform for Pharmacometrics Model Visualization and Simulation

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-plotly >= 4.10.1
BuildRequires:    R-CRAN-ggplot2 >= 3.4.4
BuildRequires:    R-CRAN-shiny >= 1.7.4.1
BuildRequires:    R-CRAN-mrgsolve >= 1.5.0
BuildRequires:    R-CRAN-data.table >= 1.14.2
BuildRequires:    R-CRAN-dplyr >= 1.1.0
BuildRequires:    R-CRAN-rlang >= 1.0.0
BuildRequires:    R-CRAN-shinyjs >= 1.0
BuildRequires:    R-CRAN-shinyWidgets >= 0.8.0
BuildRequires:    R-CRAN-shinydashboard >= 0.7.2
BuildRequires:    R-CRAN-shinyBS >= 0.61.1
BuildRequires:    R-CRAN-flextable >= 0.6.10
BuildRequires:    R-CRAN-htmltools >= 0.5.5
BuildRequires:    R-CRAN-bslib >= 0.5.1
BuildRequires:    R-CRAN-rhandsontable >= 0.3.8
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-grid 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-shinyAce 
BuildRequires:    R-CRAN-shinycssloaders 
BuildRequires:    R-CRAN-shinyFiles 
BuildRequires:    R-CRAN-shinythemes 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-zip 
Requires:         R-CRAN-plotly >= 4.10.1
Requires:         R-CRAN-ggplot2 >= 3.4.4
Requires:         R-CRAN-shiny >= 1.7.4.1
Requires:         R-CRAN-mrgsolve >= 1.5.0
Requires:         R-CRAN-data.table >= 1.14.2
Requires:         R-CRAN-dplyr >= 1.1.0
Requires:         R-CRAN-rlang >= 1.0.0
Requires:         R-CRAN-shinyjs >= 1.0
Requires:         R-CRAN-shinyWidgets >= 0.8.0
Requires:         R-CRAN-shinydashboard >= 0.7.2
Requires:         R-CRAN-shinyBS >= 0.61.1
Requires:         R-CRAN-flextable >= 0.6.10
Requires:         R-CRAN-htmltools >= 0.5.5
Requires:         R-CRAN-bslib >= 0.5.1
Requires:         R-CRAN-rhandsontable >= 0.3.8
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-DT 
Requires:         R-grid 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-shinyAce 
Requires:         R-CRAN-shinycssloaders 
Requires:         R-CRAN-shinyFiles 
Requires:         R-CRAN-shinythemes 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tidyr 
Requires:         R-tools 
Requires:         R-utils 
Requires:         R-CRAN-zip 

%description
An interactive 'shiny' application for exploring pharmacometrics models
with minimal setup. Users can explore model structures, parameters and
dosing regimens with 'mrgsolve', and compare simulations with observed
data. Additional features include parameter sensitivity analysis,
non-compartmental analysis (NCA), data exploration, variability assessment
with virtual populations, and optional AI-assisted model translation. For
design considerations of the app, see Choy et al. (2025)
<doi:10.1002/psp4.70023>.

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
