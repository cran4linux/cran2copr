%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  highMLR
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Machine Learning Feature Selection for High Dimensional Survival Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-ranger 
BuildRequires:    R-CRAN-aorsf 
BuildRequires:    R-CRAN-xgboost 
BuildRequires:    R-CRAN-stabs 
BuildRequires:    R-CRAN-survex 
BuildRequires:    R-CRAN-grf 
BuildRequires:    R-CRAN-prodlim 
BuildRequires:    R-CRAN-cmprsk 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-ranger 
Requires:         R-CRAN-aorsf 
Requires:         R-CRAN-xgboost 
Requires:         R-CRAN-stabs 
Requires:         R-CRAN-survex 
Requires:         R-CRAN-grf 
Requires:         R-CRAN-prodlim 
Requires:         R-CRAN-cmprsk 
Requires:         R-CRAN-future 
Requires:         R-CRAN-future.apply 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-utils 

%description
A unified, flexible framework for high dimensional feature selection in
the presence of a survival outcome. Provides multiple machine learning
approaches (Cox elastic net, random survival forest, accelerated oblique
random survival forest, gradient-boosted Cox, stability selection,
classical univariate Cox screening, pseudo- observation bridging to
arbitrary regression learners, and Fine-Gray competing risks selection)
under a single interface. Adds causal survival forest estimation of
heterogeneous treatment effects on survival (experimental), conformal
survival prediction with finite- sample coverage guarantees, and
time-dependent 'SHAP' explanations via 'SurvSHAP(t)'. Methodology is based
on regularised Cox regression (2011) <doi:10.18637/jss.v039.i05>, random
survival forests (2008) <doi:10.1214/08-AOAS169>, oblique random survival
forests (2024) <doi:10.1080/10618600.2023.2231048>, stability selection
(2010) <doi:10.1111/j.1467-9868.2010.00740.x>, causal survival forests
(2023) <doi:10.1111/rssb.12538>, time-dependent survival explanations
(2023) <doi:10.1016/j.knosys.2022.110234>, conformal survival prediction
(2023) <doi:10.1093/biomet/asad043>, the Fine-Gray model for competing
risks (1999) <doi:10.1080/01621459.1999.10474144>, and pseudo-observation
regression (2010) <doi:10.1177/0962280209105020>.

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
