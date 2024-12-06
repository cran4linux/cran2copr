%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  airship
%global packver   1.4.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.3
Release:          1%{?dist}%{?buildtag}
Summary:          Visualization of Simulated Datasets with Multiple Simulation Input Dimensions

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinyBS 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-shinybusy 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-colourpicker 
BuildRequires:    R-CRAN-shinyWidgets 
BuildRequires:    R-CRAN-shinydashboard 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-Cairo 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-shinyalert 
BuildRequires:    R-CRAN-vctrs 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinyBS 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-shinybusy 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-colourpicker 
Requires:         R-CRAN-shinyWidgets 
Requires:         R-CRAN-shinydashboard 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-Cairo 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-shinyalert 
Requires:         R-CRAN-vctrs 
Requires:         R-CRAN-mvtnorm 

%description
Plots simulation results of clinical trials. Its main feature is allowing
users to simultaneously investigate the impact of several simulation input
dimensions through dynamic filtering of the simulation results. A more
detailed description of the app can be found in Meyer et al.
<DOI:10.1016/j.softx.2023.101347> or the vignettes on 'GitHub'.

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
