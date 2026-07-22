%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rwevalidate
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Validate Patient Cohorts for Real-World Evidence Studies on the OMOP Common Data Model

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-RPostgres 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-utils 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-RPostgres 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-cli 
Requires:         R-utils 

%description
Validates instantiated patient cohorts on an Observational Medical
Outcomes Partnership (OMOP) Common Data Model (CDM) database for
real-world-evidence (RWE) studies. From a single function call it produces
a structured validation report in Hypertext Markup Language (HTML) and
JavaScript Object Notation (JSON) covering concept coverage, cohort
attrition, temporal data density, and covariate feasibility against a
comparator. The checks are aligned with the United States Food and Drug
Administration (FDA) guidance on real-world data and evidence, FDA (2023)
<https://www.fda.gov/media/171667/download>, the Harmonized Protocol
Template to Enhance Reproducibility (HARPER), Wang and others (2022)
<doi:10.1002/pds.5507>, and the Reporting of Studies Conducted Using
Observational Routinely-Collected Data for Pharmacoepidemiology
(RECORD-PE) statement, Langan and others (2018) <doi:10.1136/bmj.k3532>. A
self-contained example database is bundled so the checks can be run
without a live database connection.

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
