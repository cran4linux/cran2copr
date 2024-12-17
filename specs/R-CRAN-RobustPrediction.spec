%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RobustPrediction
%global packver   0.1.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.7
Release:          1%{?dist}%{?buildtag}
Summary:          Robust Tuning and Training for Cross-Source Prediction

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-mboost 
BuildRequires:    R-CRAN-mlr 
BuildRequires:    R-CRAN-ranger 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-pROC 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-mboost 
Requires:         R-CRAN-mlr 
Requires:         R-CRAN-ranger 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-pROC 

%description
Provides robust parameter tuning and model training for predictive models
applied across data sources where the data distribution varies slightly
from source to source. This package implements three primary tuning
methods: cross-validation-based internal tuning, external tuning, and the
'RobustTuneC' method. External tuning includes a conservative option where
parameters are tuned internally on the training data and validating on an
external dataset, providing a slightly pessimistic estimate. It supports
Lasso, Ridge, Random Forest, Boosting, and Support Vector Machine
classifiers. Currently, only binary classification is supported. The
response variable must be the first column of the dataset and a factor
with exactly two levels. The tuning methods are based on the paper by
Nicole Ellenbach, Anne-Laure Boulesteix, Bernd Bischl, Kristian Unger, and
Roman Hornung (2021) "Improved Outcome Prediction Across Data Sources
Through Robust Parameter Tuning" <doi:10.1007/s00357-020-09368-z>.

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
