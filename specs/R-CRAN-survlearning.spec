%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  survlearning
%global packver   0.3.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.5
Release:          1%{?dist}%{?buildtag}
Summary:          Unified Statistical Learning for Survival and Reliability

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildRequires:    R-CRAN-glmnet >= 5.0
BuildRequires:    R-CRAN-xgboost >= 3.0.0
BuildRequires:    R-CRAN-withr >= 2.5.0
BuildRequires:    R-CRAN-osqp >= 1.0.0
BuildRequires:    R-CRAN-MTLR >= 0.2.2
BuildRequires:    R-CRAN-clarabel >= 0.11.3
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-rpart 
BuildRequires:    R-CRAN-gbm 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-irlba 
BuildRequires:    R-CRAN-CoxBoost 
BuildRequires:    R-CRAN-ranger 
BuildRequires:    R-CRAN-aorsf 
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-nnet 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-glmnet >= 5.0
Requires:         R-CRAN-xgboost >= 3.0.0
Requires:         R-CRAN-withr >= 2.5.0
Requires:         R-CRAN-osqp >= 1.0.0
Requires:         R-CRAN-MTLR >= 0.2.2
Requires:         R-CRAN-clarabel >= 0.11.3
Requires:         R-stats 
Requires:         R-CRAN-survival 
Requires:         R-graphics 
Requires:         R-utils 
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-tools 
Requires:         R-CRAN-rpart 
Requires:         R-CRAN-gbm 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-irlba 
Requires:         R-CRAN-CoxBoost 
Requires:         R-CRAN-ranger 
Requires:         R-CRAN-aorsf 
Requires:         R-splines 
Requires:         R-CRAN-nnet 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-quadprog 

%description
Provides a small formula-based interface for fitting, tuning, predicting,
and comparing statistical learning models for right-censored survival and
reliability data. Provides censoring-aware evaluation, reusable
stratified, grouped and temporal validation, and nested tuning. Supports
paired assessment intervals, censoring-weighted calibration measures and
cross-validated convex combinations of survival curves. Distinguishes risk
scores, survival probabilities and median survival times. Includes
reference models, forests, boosting and neural survival models through
integrated engines, with training-only preprocessing and explicit
prediction capabilities. Methodological references include Simon et al.
(2011) <doi:10.18637/jss.v039.i05> for penalized Cox regression and
Ishwaran et al. (2008) <doi:10.1214/08-AOAS169> for random survival
forests.

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
