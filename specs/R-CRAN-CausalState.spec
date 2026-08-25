%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CausalState
%global packver   0.10.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.10.2
Release:          1%{?dist}%{?buildtag}
Summary:          Causal Inference in a Longitudinal Transitioning State Environment

License:          AGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table >= 1.14.0
BuildRequires:    R-CRAN-SuperLearner 
BuildRequires:    R-CRAN-origami 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-xgboost 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
Requires:         R-CRAN-data.table >= 1.14.0
Requires:         R-CRAN-SuperLearner 
Requires:         R-CRAN-origami 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-xgboost 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-magrittr 
Requires:         R-parallel 
Requires:         R-stats 

%description
Implements Sequential Doubly Robust (SDR) and infinite-dimensional
Targeted Maximum Likelihood (iTMLE) estimators for longitudinal modified
treatment policies in settings with transitioning states, such as ICU,
ward, or emergency department care episodes. Treatment is permitted in
active states and becomes structurally inapplicable after a state
transition (e.g. discharge or death). Supports asymmetric g- and Q-model
regularisation, k-fold cross-fitting, and pluggable SuperLearner
ensembles. Includes specialised SuperLearner wrappers (SL.tgt.* and
SL.tmle_* families) for the iTMLE targeting step, which pass the logit
offset as a covariate column to preserve correct subsetting during
SuperLearner cross-validation. Methods based on Diaz et al. (2021)
<doi:10.1080/01621459.2021.1955691> and Luedtke et al. (2017)
<doi:10.48550/arXiv.1705.02459>.

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
