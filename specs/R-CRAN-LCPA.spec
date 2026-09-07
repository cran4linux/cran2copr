%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  LCPA
%global packver   1.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          1%{?dist}%{?buildtag}
Summary:          A General Framework for Latent Class and Profile Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-reticulate 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-CompQuadForm 
BuildRequires:    R-CRAN-clue 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-MplusAutomation 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-reticulate 
Requires:         R-methods 
Requires:         R-CRAN-CompQuadForm 
Requires:         R-CRAN-clue 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-MplusAutomation 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-nloptr 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-scales 

%description
Provides a unified framework for finite-mixture latent variable models,
including latent class analysis (LCA), latent profile analysis (LPA),
latent class/profile analysis with covariates, and latent transition
analysis (LTA), within one consistent interface. Estimation methods
include the expectation-maximization (EM) algorithm; neural network
estimation, which requires 'Python' and its dependent libraries;
integration with 'Mplus', which requires an installed copy of 'Mplus'; and
stochastic EM (SEM) through the optional 'flexmix', 'Rmixmod', and
'RMixtComp' backends. 'flexmix' and the default 'Rmixmod' path perform
configurable warm-up trajectories and promote the best candidates to full
SEM replications. 'Rmixmod' additionally exposes its native strategy
interface, including chained SEM-to-EM estimation, whereas 'RMixtComp'
exposes its native SEM and Gibbs controls without the external warm-up
stage. Model assessment includes the Akaike information criterion (AIC),
Bayesian information criterion (BIC), Schwarz information criterion (SIC),
consistent AIC (CAIC), approximate weight of evidence (AWE),
sample-size-adjusted BIC (SABIC), entropy, and average posterior
probabilities. Model-comparison procedures include the ordinary
likelihood-ratio test, the Mplus TECH11 Vuong-Lo-Mendell-Rubin and
adjusted Lo-Mendell-Rubin tests, and fixed-replicate or sequential
parametric bootstrap likelihood-ratio tests. Standard errors can be
estimated by nonparametric bootstrap, numerical observed information, or
analytic observed information based on Louis' identity.
Classification-error-adjusted maximum-likelihood and Bolck-Croon-Hagenaars
three-step methods support covariates predicting latent membership,
initial-status and transition regressions, and latent classes or states
predicting continuous and categorical external observed dependent
variables. Simulation, posterior-probability, classification-error,
extraction, summary, plotting, model-adjustment, and update utilities are
also provided for reproducible workflows.

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
