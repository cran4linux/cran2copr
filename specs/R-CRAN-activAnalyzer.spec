%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  activAnalyzer
%global packver   2.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          A 'Shiny' App to Analyze Accelerometer-Measured Daily Physical Behavior Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-rmarkdown >= 2.16
BuildRequires:    R-CRAN-dbplyr >= 2.1.1
BuildRequires:    R-CRAN-shinyjs >= 2.1.0
BuildRequires:    R-CRAN-magrittr >= 2.0.3
BuildRequires:    R-CRAN-shinydashboardPlus >= 2.0.3
BuildRequires:    R-CRAN-plyr >= 1.8.7
BuildRequires:    R-CRAN-lubridate >= 1.8.0
BuildRequires:    R-CRAN-shiny >= 1.7.2
BuildRequires:    R-CRAN-stringr >= 1.4.1
BuildRequires:    R-CRAN-tidyr >= 1.2.1
BuildRequires:    R-CRAN-hms >= 1.1.2
BuildRequires:    R-CRAN-patchwork >= 1.1.2
BuildRequires:    R-CRAN-dplyr >= 1.1.0
BuildRequires:    R-CRAN-shinycssloaders >= 1.0.0
BuildRequires:    R-CRAN-flextable >= 0.8.2
BuildRequires:    R-CRAN-shinydashboard >= 0.7.2
BuildRequires:    R-CRAN-forcats >= 0.5.2
BuildRequires:    R-CRAN-shinyFeedback >= 0.4.0
BuildRequires:    R-CRAN-golem >= 0.3.4
BuildRequires:    R-CRAN-reactable >= 0.3.0
BuildRequires:    R-CRAN-modelr >= 0.1.9
BuildRequires:    R-CRAN-PhysicalActivity 
BuildRequires:    R-CRAN-RSQLite 
BuildRequires:    R-CRAN-zoo 
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-rmarkdown >= 2.16
Requires:         R-CRAN-dbplyr >= 2.1.1
Requires:         R-CRAN-shinyjs >= 2.1.0
Requires:         R-CRAN-magrittr >= 2.0.3
Requires:         R-CRAN-shinydashboardPlus >= 2.0.3
Requires:         R-CRAN-plyr >= 1.8.7
Requires:         R-CRAN-lubridate >= 1.8.0
Requires:         R-CRAN-shiny >= 1.7.2
Requires:         R-CRAN-stringr >= 1.4.1
Requires:         R-CRAN-tidyr >= 1.2.1
Requires:         R-CRAN-hms >= 1.1.2
Requires:         R-CRAN-patchwork >= 1.1.2
Requires:         R-CRAN-dplyr >= 1.1.0
Requires:         R-CRAN-shinycssloaders >= 1.0.0
Requires:         R-CRAN-flextable >= 0.8.2
Requires:         R-CRAN-shinydashboard >= 0.7.2
Requires:         R-CRAN-forcats >= 0.5.2
Requires:         R-CRAN-shinyFeedback >= 0.4.0
Requires:         R-CRAN-golem >= 0.3.4
Requires:         R-CRAN-reactable >= 0.3.0
Requires:         R-CRAN-modelr >= 0.1.9
Requires:         R-CRAN-PhysicalActivity 
Requires:         R-CRAN-RSQLite 
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
