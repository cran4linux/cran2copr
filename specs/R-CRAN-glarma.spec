%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  glarma
%global packver   1.7-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7.1
Release:          1%{?dist}%{?buildtag}
Summary:          Generalized Linear Autoregressive Moving Average Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.3.0
Requires:         R-core >= 2.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-methods 
Requires:         R-CRAN-MASS 
Requires:         R-methods 

%description
Functions are provided for estimation, testing, diagnostic checking and
forecasting of generalized linear autoregressive moving average (GLARMA)
models for discrete valued time series with regression variables.  These
are a class of observation driven non-linear non-Gaussian state space
models. The state vector consists of a linear regression component plus an
observation driven component consisting of an autoregressive-moving
average (ARMA) filter of past predictive residuals. Currently three
distributions (Poisson, negative binomial and binomial) can be used for
the response series. Three options (Pearson, score-type and unscaled) for
the residuals in the observation driven component are available.
Estimation is via maximum likelihood (conditional on initializing values
for the ARMA process) optimized using Fisher scoring or Newton Raphson
iterative methods. Likelihood ratio and Wald tests for the observation
driven component allow testing for serial dependence in generalized linear
model settings. Graphical diagnostics including model fits,
autocorrelation functions and probability integral transform residuals are
included in the package. Several standard data sets are included in the
package.

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
