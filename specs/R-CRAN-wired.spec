%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  wired
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Weighted Adaptive Prediction with Structured Dependence

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-forecast >= 8.24.0
BuildRequires:    R-CRAN-MASS >= 7.3.65
BuildRequires:    R-CRAN-quantreg >= 6.1
BuildRequires:    R-CRAN-imputeTS >= 3.4
BuildRequires:    R-CRAN-mc2d >= 0.2.1
Requires:         R-CRAN-forecast >= 8.24.0
Requires:         R-CRAN-MASS >= 7.3.65
Requires:         R-CRAN-quantreg >= 6.1
Requires:         R-CRAN-imputeTS >= 3.4
Requires:         R-CRAN-mc2d >= 0.2.1

%description
Builds a joint probabilistic forecast across series and horizons using
adaptive copulas (Gaussian/t) with shrinkage-repaired correlations. At the
low level it calls a probabilistic mixer per series and horizon, which
backtests several simple predictors, predicts next-window Continuous
Ranked Probability Score (CRPS), and converts those scores into softmax
weights to form a calibrated mixture (r/q/p/dfun). The mixer blends eight
simple predictors: a naive predictor that wraps the last move in a PERT
distribution; an arima predictor using auto.arima for one-step forecasts;
an Exponentially Weighted Moving Average (EWMA) gaussian predictor with
mean/variance under a Gaussian; a historical bootstrap predictor that
resamples past horizon-aligned moves; a drift residual bootstrap predictor
combining linear trend with bootstrapped residuals; a volatility-scaled
naive predictor centering on the last move and scaling by recent
volatility; a robust median mad predictor using median/MAD with Laplace or
Normal shape; and a shrunk quantile predictor that fits a few quantile
regressions over time and interpolates to a full predictive. The function
then couples the per-series mixtures on a common transform
(additive/multiplicative/log-multiplicative), simulates coherent draws,
and returns both transformed- and level-scale samplers and summaries.

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
