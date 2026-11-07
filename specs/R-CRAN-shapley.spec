%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  shapley
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Weighted Mean SHAP and CI for Robust Feature Assessment in ML Grid

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.4.2
BuildRequires:    R-CRAN-h2o >= 3.34.0.0
BuildRequires:    R-CRAN-kernelshap >= 0.9.1
BuildRequires:    R-CRAN-pander >= 0.6.5
BuildRequires:    R-CRAN-treeshap >= 0.4.0
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 >= 3.4.2
Requires:         R-CRAN-h2o >= 3.34.0.0
Requires:         R-CRAN-kernelshap >= 0.9.1
Requires:         R-CRAN-pander >= 0.6.5
Requires:         R-CRAN-treeshap >= 0.4.0
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-utils 

%description
This R package introduces Weighted Mean SHapley Additive exPlanations
(WMSHAP), a framework for estimating and combining SHAP values across a
grid of fine-tuned machine learning models or the base learners of stacked
ensembles. Rather than relying on a single best-performing model, WMSHAP
combines SHAP values from multiple models, weighting their contributions
according to predictive performance. Model weights can be calculated using
R-squared for regression and classification models or, for binary
classifiers, the area under the precision-recall curve (AUCPR), the area
under the receiver operating characteristic curve (AUC), or the F2 score.
The package also provides weighted confidence intervals for mean SHAP
values, allowing feature importance to be evaluated across multiple models
while accounting for variability in their contributions. This approach
particularly improves accuracy if feature importance assessment at both
local (individual) and global (feature) levels and improves the stability
of feature importance rankins (see the GitHub repository for references
and details). By integrating SHAP values across models, WMSHAP reduces
reliance on any single potentially overfitted or biased model, providing a
more comprehensive and generalizable assessment of feature importance. The
package further implements hypothesis tests to assess the statistical
significance of individual feature contributions, as well as comparative
tests to evaluate differences in SHAP contributions between features. It
also provides criteria for automatic feature selection across model grids
and stacked ensembles, eliminating the need to specify an arbitrary number
of top features. This approach supports a more representative assessment
of feature importance by considering evidence from multiple models rather
than relying exclusively on the best-performing model. The package also
provides visualizations of SHAP values at individual, feature, and factor
levels, including feature-selection plots based on weighted mean WMSHAP
ratios. Supported SHAP backends include 'h2o', 'treeshap', 'shapr', and
'kernelshap', as well as native 'gpboost' explanations of the boosted-tree
component.

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
