%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  OdysseusPathwayModule
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Cohort Pathway Analysis with Pre-Index Event Support

License:          Apache License (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-DatabaseConnector 
BuildRequires:    R-CRAN-SqlRender 
Requires:         R-CRAN-DatabaseConnector 
Requires:         R-CRAN-SqlRender 

%description
Provides cohort pathway analysis for Observational Medical Outcomes
Partnership (OMOP) Common Data Model databases, including both standard
(post-index) and pre-index pathway analyses. The pre-index analysis
identifies sequences of events occurring in a lookback window before the
target cohort index date. Built on the 'CohortPathways' analysis framework
originally developed by Christopher Knoll and the Observational Health
Data Sciences and Informatics community through 'WebAPI'. Methodological
background and the originating implementation are described in
<https://github.com/OHDSI/CohortPathways>.

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
