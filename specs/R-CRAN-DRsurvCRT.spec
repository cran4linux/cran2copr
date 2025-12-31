%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DRsurvCRT
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Doubly-Robust Estimation for Survival Outcomes in Cluster-Randomized Trials

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-frailtyEM 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-frailtyEM 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-abind 

%description
Cluster-randomized trials (CRTs) assign treatment to groups rather than
individuals, so valid analyses must distinguish cluster-level and
individual-level effects and define estimands within a potential-outcomes
framework. This package supports right-censored survival outcomes for both
single-state (binary) and multi-state settings. For single-state outcomes,
it provides estimands based on stage-specific survival contrasts (SPCE)
and restricted mean survival time (RMST). For multi-state outcomes, it
provides SPCE as well as a generalized win-based restricted mean
time-in-favor estimand (RMT-IF). The package implements doubly robust
estimators that accommodate covariate-dependent censoring and remain
consistent if either the outcome model or the censoring model is correctly
specified. Users can choose marginal Cox or gamma-frailty Cox working
models for nuisance estimation, and inference is supported via
leave-one-cluster-out jackknife variance and confidence interval
estimation. Methods are described in Fang et al. (2025) "Estimands and
doubly robust estimation for cluster-randomized trials with survival
outcomes" <doi:10.48550/arXiv.2510.08438>.

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
