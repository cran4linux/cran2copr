%global __brp_check_rpaths %{nil}
%global packname  walker
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Generalized Linear Models with Time-Varying Coefficients

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-rstan >= 2.18.1
BuildRequires:    R-CRAN-StanHeaders >= 2.18.0
BuildRequires:    R-CRAN-rstantools >= 2.0.0
BuildRequires:    R-CRAN-BH >= 1.66.0
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.3.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.9
BuildRequires:    R-CRAN-bayesplot 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-KFAS 
BuildRequires:    R-CRAN-loo 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RcppParallel 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-rstantools
Requires:         R-CRAN-rstan >= 2.18.1
Requires:         R-CRAN-rstantools >= 2.0.0
Requires:         R-CRAN-Rcpp >= 0.12.9
Requires:         R-CRAN-bayesplot 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-KFAS 
Requires:         R-CRAN-loo 
Requires:         R-methods 
Requires:         R-CRAN-RcppParallel 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-rstantools

%description
Bayesian generalized linear models with time-varying coefficients as in
Helske (2020, <arXiv:2009.07063>). Gaussian, Poisson, and binomial
observations are supported. The Markov chain Monte Carlo (MCMC)
computations are done using Hamiltonian Monte Carlo provided by Stan,
using a state space representation of the model in order to marginalise
over the coefficients for efficient sampling. For non-Gaussian models, the
package uses the importance sampling type estimators based on approximate
marginal MCMC as in Vihola, Helske, Franks (2020,
<doi:10.1111/sjos.12492>).

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
