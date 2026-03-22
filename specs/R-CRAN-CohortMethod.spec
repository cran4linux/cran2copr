%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CohortMethod
%global packver   6.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          6.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Comparative Cohort Method with Large Scale Propensity and Outcome Models

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-DatabaseConnector >= 6.0.0
BuildRequires:    R-CRAN-Cyclops >= 3.6.0
BuildRequires:    R-CRAN-ParallelLogger >= 3.4.2
BuildRequires:    R-CRAN-FeatureExtraction >= 3.0.0
BuildRequires:    R-CRAN-SqlRender >= 1.18.0
BuildRequires:    R-CRAN-Andromeda >= 0.6.3
BuildRequires:    R-CRAN-Rcpp >= 0.11.2
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-EmpiricalCalibration 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-digest 
Requires:         R-CRAN-DatabaseConnector >= 6.0.0
Requires:         R-CRAN-Cyclops >= 3.6.0
Requires:         R-CRAN-ParallelLogger >= 3.4.2
Requires:         R-CRAN-FeatureExtraction >= 3.0.0
Requires:         R-CRAN-SqlRender >= 1.18.0
Requires:         R-CRAN-Andromeda >= 0.6.3
Requires:         R-CRAN-Rcpp >= 0.11.2
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 
Requires:         R-grid 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-EmpiricalCalibration 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-digest 

%description
Functions for performing comparative cohort studies in an observational
database in the Observational Medical Outcomes Partnership (OMOP) Common
Data Model. Can extract all necessary data from a database. This
implements large-scale propensity scores (LSPS) as described in Tian et
al. (2018) <doi:10.1093/ije/dyy120>, using a large set of covariates,
including for example all drugs, diagnoses, procedures, as well as age,
comorbidity indexes, etc. Large scale regularized regression is used to
fit the propensity and outcome models as described in Suchard et al.
(2013) <doi:10.1145/2414416.2414791>. Functions are included for trimming,
stratifying, (variable and fixed ratio) matching and weighting by
propensity scores, as well as diagnostic functions, such as propensity
score distribution plots and plots showing covariate balance before and
after matching and/or trimming. Supported outcome models are (conditional)
logistic regression, (conditional) Poisson regression, and (stratified)
Cox regression. Also included are Kaplan-Meier plots that can adjust for
the stratification or matching.

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
