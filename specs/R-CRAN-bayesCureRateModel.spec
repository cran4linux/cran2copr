%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bayesCureRateModel
%global packver   1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Cure Rate Modeling for Time-to-Event Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.12
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-HDInterval 
BuildRequires:    R-CRAN-VGAM 
BuildRequires:    R-CRAN-calculus 
BuildRequires:    R-CRAN-flexsurv 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 1.0.12
Requires:         R-CRAN-survival 
Requires:         R-CRAN-doParallel 
Requires:         R-parallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-mclust 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-HDInterval 
Requires:         R-CRAN-VGAM 
Requires:         R-CRAN-calculus 
Requires:         R-CRAN-flexsurv 

%description
A fully Bayesian approach in order to estimate a general family of cure
rate models under the presence of covariates, see Papastamoulis and
Milienos (2024) <doi:10.1007/s11749-024-00942-w>. The promotion time can
be modelled (a) parametrically using typical distributional assumptions
for time to event data (including the Weibull, Exponential, Gompertz,
log-Logistic distributions), or (b) semiparametrically using finite
mixtures of distributions. In both cases, user-defined families of
distributions are allowed under some specific requirements. Posterior
inference is carried out by constructing a Metropolis-coupled Markov chain
Monte Carlo (MCMC) sampler, which combines Gibbs sampling for the latent
cure indicators and Metropolis-Hastings steps with Langevin diffusion
dynamics for parameter updates. The main MCMC algorithm is embedded within
a parallel tempering scheme by considering heated versions of the target
posterior distribution.

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
