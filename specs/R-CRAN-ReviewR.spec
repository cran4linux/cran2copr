%global __brp_check_rpaths %{nil}
%global packname  ReviewR
%global packver   2.3.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3.8
Release:          1%{?dist}%{?buildtag}
Summary:          A Light-Weight, Portable Tool for Reviewing Individual Patient Records

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-shinydashboardPlus >= 2.0.0
BuildRequires:    R-CRAN-shiny >= 1.5.0
BuildRequires:    R-CRAN-bigrquery >= 1.2.0
BuildRequires:    R-CRAN-tidyr >= 1.1.0
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-shinycssloaders >= 1.0.0
BuildRequires:    R-CRAN-shinyWidgets >= 0.6.0
BuildRequires:    R-CRAN-rlang >= 0.4.7
BuildRequires:    R-CRAN-config 
BuildRequires:    R-CRAN-dashboardthemes 
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-dbplyr 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-gargle 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-golem 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-redcapAPI 
BuildRequires:    R-CRAN-REDCapR 
BuildRequires:    R-CRAN-RPostgres 
BuildRequires:    R-CRAN-RSQLite 
BuildRequires:    R-CRAN-shinydashboard 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-snakecase 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-shinydashboardPlus >= 2.0.0
Requires:         R-CRAN-shiny >= 1.5.0
Requires:         R-CRAN-bigrquery >= 1.2.0
Requires:         R-CRAN-tidyr >= 1.1.0
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-shinycssloaders >= 1.0.0
Requires:         R-CRAN-shinyWidgets >= 0.6.0
Requires:         R-CRAN-rlang >= 0.4.7
Requires:         R-CRAN-config 
Requires:         R-CRAN-dashboardthemes 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-dbplyr 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-gargle 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-golem 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-redcapAPI 
Requires:         R-CRAN-REDCapR 
Requires:         R-CRAN-RPostgres 
Requires:         R-CRAN-RSQLite 
Requires:         R-CRAN-shinydashboard 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-snakecase 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tibble 

%description
A portable Shiny tool to explore patient-level electronic health record
data and perform chart review in a single integrated framework. This tool
supports browsing clinical data in many different formats including
multiple versions of the 'OMOP' common data model as well as the
'MIMIC-III' data model. In addition, chart review information is captured
and stored securely via the Shiny interface in a 'REDCap' (Research
Electronic Data Capture) project using the 'REDCap' API. See the 'ReviewR'
website for additional information, documentation, and examples.

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
