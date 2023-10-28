%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bssm
%global packver   2.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Inference of Non-Linear and Non-Gaussian State Space Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-coda >= 0.18.1
BuildRequires:    R-CRAN-Rcpp >= 0.12.3
BuildRequires:    R-CRAN-bayesplot 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-diagis 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-posterior 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-ramcmc 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-sitmo 
Requires:         R-CRAN-coda >= 0.18.1
Requires:         R-CRAN-Rcpp >= 0.12.3
Requires:         R-CRAN-bayesplot 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-diagis 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-posterior 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tidyr 

%description
Efficient methods for Bayesian inference of state space models via Markov
chain Monte Carlo (MCMC) based on parallel importance sampling type
weighted estimators (Vihola, Helske, and Franks, 2020,
<doi:10.1111/sjos.12492>), particle MCMC, and its delayed acceptance
version. Gaussian, Poisson, binomial, negative binomial, and Gamma
observation densities and basic stochastic volatility models with
linear-Gaussian state dynamics, as well as general non-linear Gaussian
models and discretised diffusion models are supported. See Helske and
Vihola (2021, <doi:10.32614/RJ-2021-103>) for details.

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
