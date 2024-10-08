%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  activAnalyzer
%global packver   2.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          A 'Shiny' App to Analyze Accelerometer-Measured Daily Physical Behavior Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-dbplyr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-flextable 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-golem 
BuildRequires:    R-CRAN-hms 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-modelr 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-PhysicalActivity 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-reactable 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-RSQLite 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinycssloaders 
BuildRequires:    R-CRAN-shinydashboard 
BuildRequires:    R-CRAN-shinydashboardPlus 
BuildRequires:    R-CRAN-shinyFeedback 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-zoo 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-dbplyr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-flextable 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-golem 
Requires:         R-CRAN-hms 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-modelr 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-PhysicalActivity 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-reactable 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-RSQLite 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinycssloaders 
Requires:         R-CRAN-shinydashboard 
Requires:         R-CRAN-shinydashboardPlus 
Requires:         R-CRAN-shinyFeedback 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-zoo 

%description
A tool to analyse 'ActiGraph' accelerometer data and to implement the use
of the PROactive Physical Activity in COPD (chronic obstructive pulmonary
disease) instruments. Once analysis is completed, the app allows to export
results to .csv files and to generate a report of the measurement. All the
configured inputs relevant for interpreting the results are recorded in
the report. In addition to the existing 'R' packages that are fully
integrated with the app, the app uses some functions from the
'actigraph.sleepr' package developed by Petkova (2021)
<https://github.com/dipetkov/actigraph.sleepr/>.

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
