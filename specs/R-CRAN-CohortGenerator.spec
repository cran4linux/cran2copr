%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CohortGenerator
%global packver   0.11.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.11.1
Release:          1%{?dist}%{?buildtag}
Summary:          Cohort Generation for the OMOP Common Data Model

License:          Apache License
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-DatabaseConnector >= 5.0.0
BuildRequires:    R-CRAN-ParallelLogger >= 3.0.0
BuildRequires:    R-CRAN-readr >= 2.1.0
BuildRequires:    R-CRAN-stringi >= 1.7.6
BuildRequires:    R-CRAN-SqlRender >= 1.11.1
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-RJSONIO 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-ResultModelManager 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-DatabaseConnector >= 5.0.0
Requires:         R-CRAN-ParallelLogger >= 3.0.0
Requires:         R-CRAN-readr >= 2.1.0
Requires:         R-CRAN-stringi >= 1.7.6
Requires:         R-CRAN-SqlRender >= 1.11.1
Requires:         R-CRAN-R6 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-lubridate 
Requires:         R-methods 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-RJSONIO 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-ResultModelManager 
Requires:         R-CRAN-tibble 

%description
Generate cohorts and subsets using an Observational Medical Outcomes
Partnership (OMOP) Common Data Model (CDM) Database. Cohorts are defined
using 'CIRCE' (<https://github.com/ohdsi/circe-be>) or SQL compatible with
'SqlRender' (<https://github.com/OHDSI/SqlRender>).

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
