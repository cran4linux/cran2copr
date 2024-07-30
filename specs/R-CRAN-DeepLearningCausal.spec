%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DeepLearningCausal
%global packver   0.0.104
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.104
Release:          1%{?dist}%{?buildtag}
Summary:          Causal Inference with Super Learner and Deep Neural Networks

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ROCR 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-neuralnet 
BuildRequires:    R-CRAN-SuperLearner 
BuildRequires:    R-CRAN-class 
BuildRequires:    R-CRAN-xgboost 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-gam 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-gbm 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-weights 
Requires:         R-CRAN-ROCR 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-neuralnet 
Requires:         R-CRAN-SuperLearner 
Requires:         R-CRAN-class 
Requires:         R-CRAN-xgboost 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-gam 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-gbm 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-weights 

%description
Functions to estimate Conditional Average Treatment Effects (CATE) and
Population Average Treatment Effects on the Treated (PATT) from
experimental or observational data using the Super Learner (SL) ensemble
method and Deep neural networks. The package first provides functions to
implement meta-learners such as the Single-learner (S-learner) and
Two-learner (T-learner) described in Künzel et al. (2019)
<doi:10.1073/pnas.1804597116> for estimating the CATE. The S- and
T-learner are each estimated using the SL ensemble method and deep neural
networks. It then provides functions to implement the Ottoboni and Poulos
(2020) <doi:10.1515/jci-2018-0035> PATT-C estimator to obtain the PATT
from experimental data with noncompliance by using the SL ensemble method
and deep neural networks.

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
