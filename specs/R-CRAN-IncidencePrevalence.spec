%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  IncidencePrevalence
%global packver   0.7.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.1
Release:          1%{?dist}%{?buildtag}
Summary:          Estimate Incidence and Prevalence using the OMOP Common Data Model

License:          Apache License (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-cli >= 3.0.0
BuildRequires:    R-CRAN-zip >= 2.2.0
BuildRequires:    R-CRAN-checkmate >= 2.0.0
BuildRequires:    R-CRAN-dbplyr >= 2.0.0
BuildRequires:    R-CRAN-magrittr >= 2.0.0
BuildRequires:    R-CRAN-glue >= 1.5.0
BuildRequires:    R-CRAN-stringr >= 1.5.0
BuildRequires:    R-CRAN-CDMConnector >= 1.3.0
BuildRequires:    R-CRAN-tidyr >= 1.2.0
BuildRequires:    R-CRAN-tidyselect >= 1.2.0
BuildRequires:    R-CRAN-dplyr >= 1.1.0
BuildRequires:    R-CRAN-scales >= 1.1.0
BuildRequires:    R-CRAN-DBI >= 1.0.0
BuildRequires:    R-CRAN-lubridate >= 1.0.0
BuildRequires:    R-CRAN-rlang >= 1.0.0
BuildRequires:    R-CRAN-purrr >= 0.3.5
BuildRequires:    R-CRAN-omopgenerics 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-cli >= 3.0.0
Requires:         R-CRAN-zip >= 2.2.0
Requires:         R-CRAN-checkmate >= 2.0.0
Requires:         R-CRAN-dbplyr >= 2.0.0
Requires:         R-CRAN-magrittr >= 2.0.0
Requires:         R-CRAN-glue >= 1.5.0
Requires:         R-CRAN-stringr >= 1.5.0
Requires:         R-CRAN-CDMConnector >= 1.3.0
Requires:         R-CRAN-tidyr >= 1.2.0
Requires:         R-CRAN-tidyselect >= 1.2.0
Requires:         R-CRAN-dplyr >= 1.1.0
Requires:         R-CRAN-scales >= 1.1.0
Requires:         R-CRAN-DBI >= 1.0.0
Requires:         R-CRAN-lubridate >= 1.0.0
Requires:         R-CRAN-rlang >= 1.0.0
Requires:         R-CRAN-purrr >= 0.3.5
Requires:         R-CRAN-omopgenerics 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-tibble 

%description
Calculate incidence and prevalence using data mapped to the Observational
Medical Outcomes Partnership (OMOP) common data model. Incidence and
prevalence can be estimated for the total population in a database or for
a stratification cohort.

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
