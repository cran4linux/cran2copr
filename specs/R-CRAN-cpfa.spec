%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cpfa
%global packver   1.2-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Classification with Parallel Factor Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-multiway 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-nnet 
BuildRequires:    R-CRAN-rda 
BuildRequires:    R-CRAN-xgboost 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doParallel 
Requires:         R-CRAN-multiway 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-nnet 
Requires:         R-CRAN-rda 
Requires:         R-CRAN-xgboost 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doParallel 

%description
Classification using Richard A. Harshman's Parallel Factor Analysis-1
(Parafac) model or Parallel Factor Analysis-2 (Parafac2) model fit to a
three-way or four-way data array. See Harshman and Lundy (1994):
<doi:10.1016/0167-9473(94)90132-5>. Uses component weights from one mode
of a Parafac or Parafac2 model as features to tune parameters for one or
more classification methods via a k-fold cross-validation procedure.
Allows for constraints on different tensor modes. Supports penalized
logistic regression, support vector machine, random forest, feed-forward
neural network, regularized discriminant analysis, and gradient boosting
machine. Supports binary and multiclass classification. Predicts class
labels or class probabilities and calculates multiple classification
performance measures. Implements parallel computing via the 'parallel' and
'doParallel' packages.

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
