%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PsyML
%global packver   2.4.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.4.2
Release:          1%{?dist}%{?buildtag}
Summary:          Machine Learning Workflows for Supervised, Unsupervised, and Causal Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dials 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-hardhat 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-nnet 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-parsnip 
BuildRequires:    R-CRAN-pROC 
BuildRequires:    R-CRAN-ranger 
BuildRequires:    R-CRAN-recipes 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-rsample 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-tune 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-workflows 
BuildRequires:    R-CRAN-xgboost 
BuildRequires:    R-CRAN-yardstick 
Requires:         R-CRAN-dials 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-CRAN-hardhat 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-nnet 
Requires:         R-parallel 
Requires:         R-CRAN-parsnip 
Requires:         R-CRAN-pROC 
Requires:         R-CRAN-ranger 
Requires:         R-CRAN-recipes 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-rsample 
Requires:         R-stats 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-tune 
Requires:         R-utils 
Requires:         R-CRAN-workflows 
Requires:         R-CRAN-xgboost 
Requires:         R-CRAN-yardstick 

%description
Provides single-function pipelines for applied machine learning with
tabular data, as commonly found in psychological, behavioral, and health
research. The supervised pipeline, supervised_ml(), performs exploratory
checks, preprocessing, training of several models with cross-validation,
hyperparameter tuning, test-set evaluation, threshold optimization,
calibration, fairness analysis, decision curve analysis, and model
interpretation with permutation importance and Shapley values. The
unsupervised pipeline, unsupervised_ml(), covers k-means, hierarchical,
DBSCAN, Gaussian mixture, and latent class clustering with selection of
the number of clusters, dimensionality reduction (PCA, t-SNE, UMAP), and
anomaly detection (isolation forest, local outlier factor, Mahalanobis
distance). The causal pipeline, causal_ml(), estimates treatment effects
with propensity scores, meta-learners, double machine learning, causal
forests, and targeted maximum likelihood estimation. Also includes
learning-curve based sample size estimation, block and diversity-based
data splitting, and export of results to text and JSON.

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
