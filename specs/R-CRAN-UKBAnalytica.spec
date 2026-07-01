%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  UKBAnalytica
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          UK Biobank Data Processing and Survival Analysis Toolkit

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-pROC 
BuildRequires:    R-CRAN-tableone 
BuildRequires:    R-CRAN-mice 
BuildRequires:    R-CRAN-mitools 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-igraph 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-pROC 
Requires:         R-CRAN-tableone 
Requires:         R-CRAN-mice 
Requires:         R-CRAN-mitools 
Requires:         R-CRAN-sandwich 
Requires:         R-CRAN-lmtest 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-igraph 

%description
Provides an integrated workflow for UK Biobank Research Analysis Platform
(RAP) hosted and RAP-generated analysis tables. The package supports RAP
phenotype extraction planning, predefined variable sets and disease
definitions, standardized baseline preprocessing, multi-source endpoint
ascertainment, prevalent and incident case classification, survival-ready
cohort construction, regression, multiple imputation, propensity score
analysis, mediation analysis, subgroup and sensitivity analyses, machine
learning, proteomics enrichment and protein-protein interaction analysis,
and publication-oriented visualization. The package workflow is described
in He et al. (2026) <doi:10.64898/2026.06.19.26356057>.

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
