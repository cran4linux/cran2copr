%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MFF
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Meta Fuzzy Functions

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-xgboost 
BuildRequires:    R-CRAN-lightgbm 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-ppclust 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-xgboost 
Requires:         R-CRAN-lightgbm 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-ppclust 

%description
Implements Meta Fuzzy Functions (MFFs) for regression Tak and Ucan (2026)
<doi:10.1016/j.asoc.2026.114592> by aggregating predictions from multiple
base learners using membership weights learned in the prediction space of
validation set. The package supports fuzzy and crisp meta-ensemble
structures via Fuzzy C-Means (FCM) Tak (2018)
<doi:10.1016/j.asoc.2018.08.009>, Possibilistic FCM (PFCM) Tak (2021)
<doi:10.1016/j.ins.2021.01.024>, and k-means, and provides a workflow to
(i) generate validation/test prediction matrices from common regression
learners (linear and penalized regression via 'glmnet', random forests,
gradient boosting with 'xgboost' and 'lightgbm'), (ii) fit cluster-wise
meta fuzzy functions and compute membership-based weights, (iii) tune
clustering-related hyperparameters (number of clusters/functions,
fuzziness exponent, possibilistic regularization) via grid search on
validation loss, and (iv) predict on new/test prediction matrices and
evaluate performance using standard regression metrics (MAE, RMSE, MAPE,
SMAPE, MSE, MedAE). This enables flexible, interpretable ensemble
regression where different base models contribute to different meta
components according to learned memberships.

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
