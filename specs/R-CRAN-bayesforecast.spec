%global packname  bayesforecast
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Time Series Modeling with Stan

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-RcppParallel >= 5.0.1
BuildRequires:    R-CRAN-loo >= 2.2.0
BuildRequires:    R-CRAN-rstan >= 2.18.1
BuildRequires:    R-CRAN-StanHeaders >= 2.18.0
BuildRequires:    R-CRAN-rstantools >= 2.0.0
BuildRequires:    R-CRAN-BH >= 1.66.0
BuildRequires:    R-CRAN-bayesplot >= 1.5.0
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.3.0
BuildRequires:    R-CRAN-bridgesampling >= 0.3.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-astsa 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-prophet 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-rstantools
Requires:         R-CRAN-RcppParallel >= 5.0.1
Requires:         R-CRAN-loo >= 2.2.0
Requires:         R-CRAN-rstan >= 2.18.1
Requires:         R-CRAN-rstantools >= 2.0.0
Requires:         R-CRAN-bayesplot >= 1.5.0
Requires:         R-CRAN-bridgesampling >= 0.3.0
Requires:         R-CRAN-Rcpp >= 0.12.0
Requires:         R-methods 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-StanHeaders >= 2.18.0
Requires:         R-CRAN-astsa 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-prophet 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-rstantools

%description
Fit Bayesian time series models using 'Stan' for full Bayesian inference.
A wide range of distributions and models are supported, allowing users to
fit Seasonal ARIMA, ARIMAX, Dynamic Harmonic Regression, GARCH, t-student
innovation GARCH models, asymmetric GARCH, Random Walks, stochastic
volatility models for univariate time series.  Prior specifications are
flexible and explicitly encourage users to apply prior distributions that
actually reflect their beliefs. Model fit can easily be assessed and
compared with typical visualization methods, information criteria such as
loglik, AIC, BIC WAIC, Bayes factor and leave-one-out cross-validation
methods. References: Hyndman (2017) <doi:10.18637/jss.v027.i03>; Carpenter
et al. (2017) <doi:10.18637/jss.v076.i01>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
