%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CodelistGenerator
%global packver   3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Identify Relevant Clinical Codes and Evaluate Their Use

License:          Apache License (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.1.0
BuildRequires:    R-CRAN-checkmate >= 2.0.0
BuildRequires:    R-CRAN-magrittr >= 2.0.0
BuildRequires:    R-CRAN-glue >= 1.5.0
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-tidyselect >= 1.2.0
BuildRequires:    R-CRAN-tidyr >= 1.2.0
BuildRequires:    R-CRAN-DBI >= 1.1.0
BuildRequires:    R-CRAN-dplyr >= 1.1.0
BuildRequires:    R-CRAN-rlang >= 1.0.0
BuildRequires:    R-CRAN-PatientProfiles >= 1.0.0
BuildRequires:    R-CRAN-visOmopResults >= 0.3.0
BuildRequires:    R-CRAN-omopgenerics >= 0.2.0
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-RJSONIO 
BuildRequires:    R-CRAN-vctrs 
BuildRequires:    R-CRAN-lifecycle 
Requires:         R-CRAN-cli >= 3.1.0
Requires:         R-CRAN-checkmate >= 2.0.0
Requires:         R-CRAN-magrittr >= 2.0.0
Requires:         R-CRAN-glue >= 1.5.0
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-tidyselect >= 1.2.0
Requires:         R-CRAN-tidyr >= 1.2.0
Requires:         R-CRAN-DBI >= 1.1.0
Requires:         R-CRAN-dplyr >= 1.1.0
Requires:         R-CRAN-rlang >= 1.0.0
Requires:         R-CRAN-PatientProfiles >= 1.0.0
Requires:         R-CRAN-visOmopResults >= 0.3.0
Requires:         R-CRAN-omopgenerics >= 0.2.0
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-RJSONIO 
Requires:         R-CRAN-vctrs 
Requires:         R-CRAN-lifecycle 

%description
Generate a candidate code list for the Observational Medical Outcomes
Partnership (OMOP) common data model based on string matching. For a given
search strategy, a candidate code list will be returned.

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
