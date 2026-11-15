%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  survalis
%global packver   2.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.4.1
Release:          1%{?dist}%{?buildtag}
Summary:          Interpretable Survival Machine Learning Framework

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.4.0
Requires:         R-core >= 4.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.5.0
BuildRequires:    R-CRAN-basetable >= 1.4.5
BuildRequires:    R-CRAN-fastgbm >= 0.7.0
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-functionals 
BuildRequires:    R-CRAN-nnls 
BuildRequires:    R-CRAN-rpart 
BuildRequires:    R-CRAN-rsample 
BuildRequires:    R-CRAN-aftgee 
BuildRequires:    R-CRAN-aorsf 
BuildRequires:    R-CRAN-pec 
BuildRequires:    R-CRAN-party 
BuildRequires:    R-CRAN-ranger 
BuildRequires:    R-CRAN-unsurv 
BuildRequires:    R-CRAN-randomForestSRC 
BuildRequires:    R-CRAN-xgboost 
BuildRequires:    R-CRAN-densemlp 
BuildRequires:    R-CRAN-rpsurv 
BuildRequires:    R-CRAN-nbsurv 
BuildRequires:    R-CRAN-tvrmst 
BuildRequires:    R-CRAN-CoxBoost 
BuildRequires:    R-CRAN-BART 
BuildRequires:    R-CRAN-flexsurv 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-mboost 
BuildRequires:    R-CRAN-timereg 
BuildRequires:    R-CRAN-partykit 
BuildRequires:    R-CRAN-gower 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 >= 3.5.0
Requires:         R-CRAN-basetable >= 1.4.5
Requires:         R-CRAN-fastgbm >= 0.7.0
Requires:         R-CRAN-survival 
Requires:         R-CRAN-functionals 
Requires:         R-CRAN-nnls 
Requires:         R-CRAN-rpart 
Requires:         R-CRAN-rsample 
Requires:         R-CRAN-aftgee 
Requires:         R-CRAN-aorsf 
Requires:         R-CRAN-pec 
Requires:         R-CRAN-party 
Requires:         R-CRAN-ranger 
Requires:         R-CRAN-unsurv 
Requires:         R-CRAN-randomForestSRC 
Requires:         R-CRAN-xgboost 
Requires:         R-CRAN-densemlp 
Requires:         R-CRAN-rpsurv 
Requires:         R-CRAN-nbsurv 
Requires:         R-CRAN-tvrmst 
Requires:         R-CRAN-CoxBoost 
Requires:         R-CRAN-BART 
Requires:         R-CRAN-flexsurv 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-mboost 
Requires:         R-CRAN-timereg 
Requires:         R-CRAN-partykit 
Requires:         R-CRAN-gower 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-utils 

%description
A modular toolkit for interpretable survival machine learning with a
unified interface for fitting, prediction, evaluation, and interpretation.
It includes semiparametric, parametric, tree-based, ensemble, boosting,
kernel, and deep-learning survival learners, together with benchmarking,
scoring, calibration, and model-agnostic interpretation utilities.
Representative methodological anchors include Cox (1972)
<doi:10.1111/j.2517-6161.1972.tb00899.x>, Royston and Parmar (2002)
<doi:10.1002/sim.1203>, Ishwaran et al. (2008) <doi:10.1214/08-AOAS169>,
Jaeger et al. (2019) <doi:10.1214/19-AOAS1261>, Harrell et al. (1982)
<doi:10.1001/jama.1982.03320430047030>, Graf et al. (1999)
<doi:10.1002/(SICI)1097-0258(19990915/30)18:17/18%%3C2529::AID-SIM274%%3E3.0.CO;2-5>,
Friedman (2001) <doi:10.1214/aos/1013203451>, Apley and Zhu (2020)
<doi:10.1111/rssb.12377>, and other related methods for survival modeling,
prediction, and interpretation. Clustering of individualized survival
curves is described in El Badisy (2026) <doi:10.1093/bioadv/vbag218>.

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
