%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CohortContrast
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Enrichment Analysis of Clinically Relevant Concepts in Common Data Model Cohort Data

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-CDMConnector >= 2.0.0
BuildRequires:    R-CRAN-lubridate >= 1.9.0
BuildRequires:    R-CRAN-jsonlite >= 1.8.0
BuildRequires:    R-CRAN-omopgenerics >= 1.3.0
BuildRequires:    R-CRAN-data.table >= 1.14.0
BuildRequires:    R-CRAN-dplyr >= 1.0.4
BuildRequires:    R-CRAN-tidyr >= 1.0.0
BuildRequires:    R-CRAN-CohortConstructor >= 0.6.0
BuildRequires:    R-CRAN-nanoparquet >= 0.4.0
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-cli 
Requires:         R-CRAN-CDMConnector >= 2.0.0
Requires:         R-CRAN-lubridate >= 1.9.0
Requires:         R-CRAN-jsonlite >= 1.8.0
Requires:         R-CRAN-omopgenerics >= 1.3.0
Requires:         R-CRAN-data.table >= 1.14.0
Requires:         R-CRAN-dplyr >= 1.0.4
Requires:         R-CRAN-tidyr >= 1.0.0
Requires:         R-CRAN-CohortConstructor >= 0.6.0
Requires:         R-CRAN-nanoparquet >= 0.4.0
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-stringr 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-doParallel 
Requires:         R-parallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-cli 

%description
Identifies clinically relevant concepts in Observational Medical Outcomes
Partnership Common Data Model cohorts using an enrichment-based workflow.
Defines target and control cohorts and extracts medical interventions that
are over-represented in the target cohort during the observation period.
Users can tune filtering and selection thresholds. The workflow includes
chi-squared tests for two proportions with Yates continuity correction,
logistic tests, and hierarchy and correlation mappings for relevant
concepts. The results can be optionally explored using the bundled
graphical user interface. For workflow details and examples, see
<https://healthinformaticsut.github.io/CohortContrast/>.

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
