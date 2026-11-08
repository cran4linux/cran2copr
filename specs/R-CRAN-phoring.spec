%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  phoring
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Unified Econometric Estimation, Specification Testing, and Diagnostics

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-stats 

%description
A unified econometric toolkit providing automated specification testing,
robust covariance estimation, and publication-grade academic
visualizations. Implements ordinary and weighted least squares with
robust, cluster-robust, and heteroskedasticity and autocorrelation
consistent (HAC) standard errors; instrumental variables two-stage least
squares (2SLS); panel data estimators (within fixed effects, two-way fixed
effects, random effects GLS, first differences); binary response models
(logit and probit with average marginal effects); tobit censored
regression; count models (Poisson and negative binomial); causal inference
methods (difference-in-differences, sharp regression discontinuity);
quantile regression; dynamic time series models (autoregressive
distributed lag, Koyck distributed lag, Prais-Winsten AR(1), error
correction models, vector autoregression); and time series unit root
batteries (augmented Dickey-Fuller, Phillips-Perron, KPSS, Engle-Granger
cointegration, Granger causality, ARCH). Estimation routines integrate
comprehensive diagnostic batteries, parameter stability tests, and
academic visualizations with zero external package dependencies.

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
