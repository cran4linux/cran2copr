%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  OdysseusCharacterizationModule
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Handy and Minimalistic Common Data Model Characterization

License:          Apache License (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-DatabaseConnector 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-SqlRender 
BuildRequires:    R-stats 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-DatabaseConnector 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-SqlRender 
Requires:         R-stats 

%description
Extracts covariates from Observational Medical Outcomes Partnership (OMOP)
Common Data Model (CDM) domains using an R-only pipeline. Supports
configurable temporal windows, domain-specific covariates for drug
exposure, drug era (including Anatomical Therapeutic Chemical (ATC)
groupings), condition occurrence, condition era, concept sets and cohorts.
Methods are based on the Observational Health Data Sciences and
Informatics (OHDSI) framework described in Hripcsak et al. (2015)
<doi:10.1038/sdata.2015.35> and "The Book of OHDSI" OHDSI (2019,
ISBN:978-1-7923-0589-8).

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
