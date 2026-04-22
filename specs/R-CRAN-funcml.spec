%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  funcml
%global packver   0.7.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.1
Release:          1%{?dist}%{?buildtag}
Summary:          Functional Machine Learning Framework

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-functionals 
BuildRequires:    R-grDevices 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-nnet 
BuildRequires:    R-CRAN-rpart 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-ranger 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-gbm 
BuildRequires:    R-CRAN-C50 
BuildRequires:    R-CRAN-kknn 
BuildRequires:    R-CRAN-earth 
BuildRequires:    R-CRAN-naivebayes 
BuildRequires:    R-CRAN-mda 
BuildRequires:    R-CRAN-ada 
BuildRequires:    R-CRAN-pls 
BuildRequires:    R-CRAN-partykit 
BuildRequires:    R-CRAN-dbarts 
BuildRequires:    R-CRAN-xgboost 
BuildRequires:    R-CRAN-lightgbm 
BuildRequires:    R-CRAN-shapviz 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-methods 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-functionals 
Requires:         R-grDevices 
Requires:         R-tools 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-nnet 
Requires:         R-CRAN-rpart 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-ranger 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-gbm 
Requires:         R-CRAN-C50 
Requires:         R-CRAN-kknn 
Requires:         R-CRAN-earth 
Requires:         R-CRAN-naivebayes 
Requires:         R-CRAN-mda 
Requires:         R-CRAN-ada 
Requires:         R-CRAN-pls 
Requires:         R-CRAN-partykit 
Requires:         R-CRAN-dbarts 
Requires:         R-CRAN-xgboost 
Requires:         R-CRAN-lightgbm 
Requires:         R-CRAN-shapviz 

%description
A compact and explicit machine learning framework for supervised learning,
resampling-based evaluation, hyperparameter tuning, learner comparison,
interpretation, and plug-in g-computation. The package uses standard
formulas for model specification and provides stable S3 interfaces for
fitting, evaluation, tuning, interpretation, and causal estimation across
a learner registry with multiple backend engines. Implemented
interpretation methods build on established approaches such as
permutation-based variable importance, partial dependence, individual
conditional expectation, accumulated local effects, SHAP, and LIME; see
Friedman (2001) <doi:10.1214/aos/1013203451>, Goldstein et al. (2015)
<doi:10.1080/10618600.2014.907095>, Apley and Zhu (2020)
<doi:10.1111/rssb.12377>, Lundberg and Lee (2017)
<doi:10.48550/arXiv.1705.07874>, and Ribeiro et al. (2016)
<doi:10.48550/arXiv.1602.04938>. The framework is intentionally
opinionated: preprocessing is expected to occur outside the modeling step,
and the API emphasizes explicit inputs, consistent object contracts, and
compact interfaces rather than feature-by-feature competition with larger
machine learning ecosystems.

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
