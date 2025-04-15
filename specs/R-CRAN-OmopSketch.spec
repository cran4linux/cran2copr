%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  OmopSketch
%global packver   0.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.2
Release:          1%{?dist}%{?buildtag}
Summary:          Characterise Tables of an OMOP Common Data Model Instance

License:          Apache License (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-PatientProfiles >= 1.3.1
BuildRequires:    R-CRAN-CDMConnector >= 1.3.0
BuildRequires:    R-CRAN-omopgenerics >= 0.4.1
BuildRequires:    R-CRAN-CohortConstructor >= 0.3.1
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-clock 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-PatientProfiles >= 1.3.1
Requires:         R-CRAN-CDMConnector >= 1.3.0
Requires:         R-CRAN-omopgenerics >= 0.4.1
Requires:         R-CRAN-CohortConstructor >= 0.3.1
Requires:         R-CRAN-cli 
Requires:         R-CRAN-clock 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 

%description
Summarises key information in data mapped to the Observational Medical
Outcomes Partnership (OMOP) common data model. Assess suitability to
perform specific epidemiological studies and explore the different domains
to obtain feasibility counts and trends.

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
