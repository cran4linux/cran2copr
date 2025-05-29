%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DrugExposureDiagnostics
%global packver   1.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Diagnostics for OMOP Common Data Model Drug Records

License:          Apache License (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-magrittr >= 2.0.0
BuildRequires:    R-CRAN-checkmate >= 2.0.0
BuildRequires:    R-CRAN-glue >= 1.5.0
BuildRequires:    R-CRAN-CDMConnector >= 1.4.0
BuildRequires:    R-CRAN-tidyr >= 1.2.0
BuildRequires:    R-CRAN-tidyselect >= 1.2.0
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-rlang >= 1.0.0
BuildRequires:    R-CRAN-DrugUtilisation >= 0.7.0
BuildRequires:    R-CRAN-omopgenerics >= 0.2.3
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-clock 
Requires:         R-CRAN-magrittr >= 2.0.0
Requires:         R-CRAN-checkmate >= 2.0.0
Requires:         R-CRAN-glue >= 1.5.0
Requires:         R-CRAN-CDMConnector >= 1.4.0
Requires:         R-CRAN-tidyr >= 1.2.0
Requires:         R-CRAN-tidyselect >= 1.2.0
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-rlang >= 1.0.0
Requires:         R-CRAN-DrugUtilisation >= 0.7.0
Requires:         R-CRAN-omopgenerics >= 0.2.3
Requires:         R-CRAN-R6 
Requires:         R-CRAN-clock 

%description
Ingredient specific diagnostics for drug exposure records in the
Observational Medical Outcomes Partnership (OMOP) common data model.

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
