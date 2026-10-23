%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  nrMCmix
%global packver   0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Non-Reversible Markov Chains for Bayesian Mixture Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.12
BuildRequires:    R-base 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-salso 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 1.0.12
Requires:         R-base 
Requires:         R-CRAN-coda 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-salso 
Requires:         R-CRAN-Rdpack 
Requires:         R-stats 

%description
Provides Bayesian inference for finite and infinite mixture models using
Markov chain Monte Carlo (MCMC) methods. Supports Gaussian, multivariate
Gaussian, Poisson, Binomial, and multivariate Bernoulli mixture kernels
with different covariance structures and flexible prior specifications.
Provides tools for data generation, posterior density evaluation,
clustering and similarity analysis, and advanced MCMC sampling strategies,
including reversible and non-reversible samplers: Ascolani et al. (2026)
<doi:10.48550/arXiv.2510.03226>, informed proposals: Zanella (2020)
<doi:10.1080/01621459.2019.1585255>, collapsed Gibbs sampling: Diebolt and
Robert (1994) <doi:10.1111/j.2517-6161.1994.tb01985.x>, and
split-and-merge samplers: Dahl and Newcomb (2021)
<doi:10.1080/00949655.2021.1998502>.

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
