%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CohortCharacteristics
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Summarise and Visualise Characteristics of Patients in the OMOP CDM

License:          Apache License (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-CDMConnector >= 1.3.2
BuildRequires:    R-CRAN-PatientProfiles >= 1.0.0
BuildRequires:    R-CRAN-visOmopResults >= 0.3.0
BuildRequires:    R-CRAN-omopgenerics >= 0.2.0
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-snakecase 
BuildRequires:    R-CRAN-DiagrammeR 
Requires:         R-CRAN-CDMConnector >= 1.3.2
Requires:         R-CRAN-PatientProfiles >= 1.0.0
Requires:         R-CRAN-visOmopResults >= 0.3.0
Requires:         R-CRAN-omopgenerics >= 0.2.0
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-snakecase 
Requires:         R-CRAN-DiagrammeR 

%description
Summarise and visualise the characteristics of patients in data mapped to
the Observational Medical Outcomes Partnership (OMOP) common data model
(CDM).

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
