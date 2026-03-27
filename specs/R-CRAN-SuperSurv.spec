%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SuperSurv
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          A Unified Framework for Machine Learning Ensembles in Survival Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-nnls 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-magrittr 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-nnls 
Requires:         R-CRAN-future.apply 
Requires:         R-stats 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-magrittr 

%description
Implements a Super Learner framework for right-censored survival data. The
package fits convex combinations of parametric, semiparametric, and
machine learning survival learners by minimizing cross-validated risk
using inverse probability of censoring weighting (IPCW). It provides tools
for automated hyperparameter grid search, high-dimensional variable
screening, and evaluation of prediction performance using metrics such as
the Brier score, Uno's C-index, and time-dependent area under the curve
(AUC). Additional utilities support model interpretation for survival
ensembles, including Shapley additive explanations (SHAP), and estimation
of covariate-adjusted restricted mean survival time (RMST) contrasts. The
methodology is related to treatment-specific survival curve estimation
using machine learning described by Westling, Luedtke, Gilbert and Carone
(2024) <doi:10.1080/01621459.2023.2205060>, and the unified ensemble
framework described in Lyu et al. (2026) <doi:10.64898/2026.03.11.711010>.

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
