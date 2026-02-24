%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PhenotypeR
%global packver   0.3.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.3
Release:          1%{?dist}%{?buildtag}
Summary:          Assess Study Cohorts Using a Common Data Model

License:          Apache License (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-CodelistGenerator >= 4.0.2
BuildRequires:    R-CRAN-PatientProfiles >= 1.4.5
BuildRequires:    R-CRAN-IncidencePrevalence >= 1.2.0
BuildRequires:    R-CRAN-omopgenerics >= 1.2.0
BuildRequires:    R-CRAN-CohortCharacteristics >= 1.1.0
BuildRequires:    R-CRAN-DrugUtilisation >= 1.1.0
BuildRequires:    R-CRAN-OmopSketch >= 1.0.1
BuildRequires:    R-CRAN-CohortConstructor >= 0.5.0
BuildRequires:    R-CRAN-MeasurementDiagnostics >= 0.3.0
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-clock 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-vctrs 
Requires:         R-CRAN-CodelistGenerator >= 4.0.2
Requires:         R-CRAN-PatientProfiles >= 1.4.5
Requires:         R-CRAN-IncidencePrevalence >= 1.2.0
Requires:         R-CRAN-omopgenerics >= 1.2.0
Requires:         R-CRAN-CohortCharacteristics >= 1.1.0
Requires:         R-CRAN-DrugUtilisation >= 1.1.0
Requires:         R-CRAN-OmopSketch >= 1.0.1
Requires:         R-CRAN-CohortConstructor >= 0.5.0
Requires:         R-CRAN-MeasurementDiagnostics >= 0.3.0
Requires:         R-CRAN-cli 
Requires:         R-CRAN-clock 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-vctrs 

%description
Phenotype study cohorts in data mapped to the Observational Medical
Outcomes Partnership Common Data Model. Diagnostics are run at the
database, code list, cohort, and population level to assess whether study
cohorts are ready for research.

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
