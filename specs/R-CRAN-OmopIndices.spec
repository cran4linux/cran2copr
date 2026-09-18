%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  OmopIndices
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Patient-Level Indices from the OMOP Common Data Model

License:          Apache License (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-omopgenerics >= 1.4.0
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-clock 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-PatientProfiles 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-omopgenerics >= 1.4.0
Requires:         R-CRAN-cli 
Requires:         R-CRAN-clock 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-PatientProfiles 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rlang 

%description
Provides tools to derive standardised, reproducible patient-level indices
and covariates from Observational Medical Outcomes Partnership (OMOP)
Common Data Model (CDM) databases. Functions calculate comorbidity and
frailty scores, including the Charlson Comorbidity Index, Electronic
Frailty Index, and Hospital Frailty Risk Score, as well as body mass
index, polypharmacy, ethnicity, location, and socioeconomic status
measures.

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
