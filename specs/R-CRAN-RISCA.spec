%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RISCA
%global packver   1.0.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.6
Release:          1%{?dist}%{?buildtag}
Summary:          Causal Inference and Prediction in Cohort-Based Analyses

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-relsurv 
BuildRequires:    R-CRAN-reticulate 
BuildRequires:    R-CRAN-tune 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-statmod 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-nnet 
BuildRequires:    R-CRAN-kernlab 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-SuperLearner 
BuildRequires:    R-CRAN-rpart 
BuildRequires:    R-CRAN-mosaic 
BuildRequires:    R-CRAN-cubature 
Requires:         R-splines 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-relsurv 
Requires:         R-CRAN-reticulate 
Requires:         R-CRAN-tune 
Requires:         R-graphics 
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-statmod 
Requires:         R-parallel 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-nnet 
Requires:         R-CRAN-kernlab 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-SuperLearner 
Requires:         R-CRAN-rpart 
Requires:         R-CRAN-mosaic 
Requires:         R-CRAN-cubature 

%description
Numerous functions for cohort-based analyses, either for prediction or
causal inference. For causal inference, it includes Inverse Probability
Weighting and G-computation for marginal estimation of an exposure effect
when confounders are expected. We deal with binary outcomes,
times-to-events, competing events, and multi-state data. For multistate
data, semi-Markov model with interval censoring may be considered, and we
propose the possibility to consider the excess of mortality related to the
disease compared to reference lifetime tables. For predictive studies, we
propose a set of functions to estimate time-dependent receiver operating
characteristic (ROC) curves with the possible consideration of
right-censoring times-to-events or the presence of confounders. Finally,
several functions are available to assess time-dependent ROC curves or
survival curves from aggregated data.

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
