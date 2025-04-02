%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sae4health
%global packver   1.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Small Area Estimation for Key Health and Demographic Indicators from Household Surveys

License:          AGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3
Requires:         R-core >= 4.3
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny >= 1.7.4
BuildRequires:    R-CRAN-golem >= 0.4.1
BuildRequires:    R-CRAN-config 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-leaflet 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-shinyBS 
BuildRequires:    R-CRAN-shinydashboard 
BuildRequires:    R-CRAN-shinyFeedback 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-shinyWidgets 
BuildRequires:    R-CRAN-SUMMER 
BuildRequires:    R-CRAN-surveyPrev 
BuildRequires:    R-CRAN-survey 
BuildRequires:    R-CRAN-geodata 
BuildRequires:    R-CRAN-bookdown 
BuildRequires:    R-CRAN-markdown 
BuildRequires:    R-CRAN-haven 
BuildRequires:    R-CRAN-ggridges 
BuildRequires:    R-CRAN-ggthemes 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-viridisLite 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-leaflegend 
BuildRequires:    R-CRAN-leafsync 
BuildRequires:    R-methods 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-sn 
Requires:         R-CRAN-shiny >= 1.7.4
Requires:         R-CRAN-golem >= 0.4.1
Requires:         R-CRAN-config 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-ggplot2 
Requires:         R-grid 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-leaflet 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-shinyBS 
Requires:         R-CRAN-shinydashboard 
Requires:         R-CRAN-shinyFeedback 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-shinyWidgets 
Requires:         R-CRAN-SUMMER 
Requires:         R-CRAN-surveyPrev 
Requires:         R-CRAN-survey 
Requires:         R-CRAN-geodata 
Requires:         R-CRAN-bookdown 
Requires:         R-CRAN-markdown 
Requires:         R-CRAN-haven 
Requires:         R-CRAN-ggridges 
Requires:         R-CRAN-ggthemes 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-viridisLite 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-leaflegend 
Requires:         R-CRAN-leafsync 
Requires:         R-methods 
Requires:         R-graphics 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-sn 

%description
Enables small area estimation (SAE) of health and demographic indicators
in low- and middle-income countries (LMICs). It powers an R 'shiny'
application that helps public health analysts, policymakers, and
researchers generate subnational estimates and prevalence maps for 150+
binary indicators from Demographic and Health Surveys (DHS). Basing its
core SAE analysis workflow on the 'surveyPrev' package, the app ensures
methodological rigor through guided model selection, automated fitting,
and interactive visualization. For more details, visit
<https://sae4health.stat.uw.edu/>.

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
