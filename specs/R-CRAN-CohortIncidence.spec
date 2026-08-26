%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CohortIncidence
%global packver   4.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Cohort Incidence Analysis for the OMOP Common Data Model

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.2
Requires:         R-core >= 3.2.2
BuildArch:        noarch
BuildRequires:    R-CRAN-DatabaseConnector >= 3.0.0
BuildRequires:    R-CRAN-SqlRender >= 1.6.0
BuildRequires:    R-CRAN-rJava >= 0.9.10
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-jsonlite 
Requires:         R-CRAN-DatabaseConnector >= 3.0.0
Requires:         R-CRAN-SqlRender >= 1.6.0
Requires:         R-CRAN-rJava >= 0.9.10
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-jsonlite 

%description
Provides functionality for performing cohort incidence analyses against
data stored in the OMOP Common Data Model (CDM). The package generates
database-specific SQL, executes analyses across supported database
platforms, and returns standardized incidence estimates using configurable
time-at-risk, stratification, and cohort definitions. It is intended to
support reproducible observational research within the OHDSI analytics
framework.

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
