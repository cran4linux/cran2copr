%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  wARMASVp
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Winsorized ARMA Estimation for Higher-Order Stochastic Volatility Models

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 1.0.0
BuildRequires:    R-CRAN-gsignal 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 1.0.0
Requires:         R-CRAN-gsignal 
Requires:         R-stats 

%description
Estimation, simulation, hypothesis testing, AR-order selection, and
forecasting for univariate higher-order stochastic volatility SV(p)
models. Supports Gaussian, Student-t, and Generalized Error Distribution
(GED) innovations, with optional leverage effects. Estimation uses
closed-form Winsorized ARMA-SV (W-ARMA-SV) moment-based methods that avoid
numerical optimization. Hypothesis testing includes Local Monte Carlo
(LMC) and Maximized Monte Carlo (MMC) procedures for leverage effects,
heavy tails, and autoregressive order. AR-order selection is also
available via information criteria (BIC/AIC) using the Kalman-filter
quasi-likelihood and the Hannan-Rissanen ARMA residual variance.
Forecasting is based on Kalman filtering and smoothing. See Ahsan and
Dufour (2021) <doi:10.1016/j.jeconom.2021.03.008>, Ahsan, Dufour, and
Rodriguez-Rondon (2025) <doi:10.1111/jtsa.12851>, and Ahsan, Dufour, and
Rodriguez-Rondon (2026) <doi:10.34989/swp-2026-8> for details.

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
