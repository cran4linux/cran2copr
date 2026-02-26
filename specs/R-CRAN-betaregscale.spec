%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  betaregscale
%global packver   2.6.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.6.9
Release:          1%{?dist}%{?buildtag}
Summary:          Beta Regression for Interval-Censored Scale-Derived Outcomes

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.12
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-Rcpp >= 1.0.12
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-rlang 
Requires:         R-stats 

%description
Maximum-likelihood estimation of beta regression models for responses
derived from bounded rating scales. Observations are treated as
interval-censored on (0, 1) after a scale-to-unit transformation, and the
likelihood is built from the difference of the beta CDF at the interval
endpoints. The complete likelihood supports mixed censoring types:
uncensored, left-censored, right-censored, and interval-censored
observations. Both fixed- and variable-dispersion submodels are supported,
with flexible link functions for the mean and precision components. A
compiled C++ backend (via 'Rcpp' and 'RcppArmadillo') provides numerically
stable, high-performance log-likelihood evaluation. Standard S3 methods
(print(), summary(), coef(), fitted(), residuals(), predict(), plot(),
confint(), vcov(), logLik(), AIC(), BIC()) are available for fitted
objects.

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
