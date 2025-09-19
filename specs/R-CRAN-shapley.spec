%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  shapley
%global packver   0.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.1
Release:          1%{?dist}%{?buildtag}
Summary:          Weighted Mean SHAP and CI for Robust Feature Assessment in ML Grid

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-curl >= 4.3.0
BuildRequires:    R-CRAN-ggplot2 >= 3.4.2
BuildRequires:    R-CRAN-h2o >= 3.34.0.0
BuildRequires:    R-CRAN-pander >= 0.6.5
Requires:         R-CRAN-curl >= 4.3.0
Requires:         R-CRAN-ggplot2 >= 3.4.2
Requires:         R-CRAN-h2o >= 3.34.0.0
Requires:         R-CRAN-pander >= 0.6.5

%description
This R package introduces Weighted Mean SHapley Additive exPlanations
(WMSHAP), an innovative method for calculating SHAP values for a grid of
fine-tuned base-learner machine learning models as well as stacked
ensembles, a method not previously available due to the common reliance on
single best-performing models. By integrating the weighted mean SHAP
values from individual base-learners comprising the ensemble or individual
base-learners in a tuning grid search, the package weights SHAP
contributions according to each model's performance, assessed by multiple
either R squared (for both regression and classification models).
alternatively, this software also offers weighting SHAP values based on
the area under the precision-recall curve (AUCPR), the area under the
curve (AUC), and F2 measures for binary classifiers. It further extends
this framework to implement weighted confidence intervals for weighted
mean SHAP values, offering a more comprehensive and robust feature
importance evaluation over a grid of machine learning models, instead of
solely computing SHAP values for the best model. This methodology is
particularly beneficial for addressing the severe class imbalance (class
rarity) problem by providing a transparent, generalized measure of feature
importance that mitigates the risk of reporting SHAP values for an
overfitted or biased model and maintains robustness under severe class
imbalance, where there is no universal criteria of identifying the
absolute best model. Furthermore, the package implements hypothesis
testing to ascertain the statistical significance of SHAP values for
individual features, as well as comparative significance testing of SHAP
contributions between features. Additionally, it tackles a critical gap in
feature selection literature by presenting criteria for the automatic
feature selection of the most important features across a grid of models
or stacked ensembles, eliminating the need for arbitrary determination of
the number of top features to be extracted. This utility is invaluable for
researchers analyzing feature significance, particularly within severely
imbalanced outcomes where conventional methods fall short. Moreover, it is
also expected to report democratic feature importance across a grid of
models, resulting in a more comprehensive and generalizable feature
selection. The package further implements a novel method for visualizing
SHAP values both at subject level and feature level as well as a plot for
feature selection based on the weighted mean SHAP ratios.

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
