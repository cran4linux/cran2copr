%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RobustLPA
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Robust Latent Profile Analysis

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-bayesplot 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-ggplot2 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-bayesplot 
Requires:         R-CRAN-coda 

%description
Provides a comprehensive toolset for estimating Latent Profile Analysis
(LPA) models that are robust to multivariate outliers and missing data. By
integrating a high-performance 'C++' engine via 'RcppArmadillo', it
reliably extracts latent profiles using both Expectation-Maximization (EM)
and Markov Chain Monte Carlo (MCMC) Bayesian estimation. Robustness is
obtained either by Huber-type down-weighting or by mixtures of
multivariate t distributions (a likelihood-based robust model, see Peel
and McLachlan (2000) <doi:10.1023/A:1008981510081>). Missing data are
handled by full information maximum likelihood with the exact EM treatment
of incomplete observations (data augmentation in the MCMC engine). The EM
engine also supports LASSO regularization with k-fold cross-validation for
penalty tuning; the MCMC engine uses a Bayesian Lasso with Laplace priors,
multiple chains, Gelman-Rubin/effective sample size diagnostics and the
widely applicable information criterion. It supports six geometric
variance-covariance models, along with functions for bootstrapped
likelihood ratio tests (BLRT), BCH auxiliary variable analysis, and
plotting. For longitudinal data, it fits robust growth mixture models and
latent class growth analysis (Muthen and Shedden (1999)
<doi:10.1111/j.0006-341X.1999.00463.x>) for one or several outcomes
measured on unbalanced occasions, with Gaussian, Huber-weighted or
multivariate-t (Pinheiro, Liu and Wu (2001)
<doi:10.1198/10618600152628059>) latent classes, by EM and MCMC, and
optional adaptive LASSO penalties (Zou (2006)
<doi:10.1198/016214506000000735>) that identify stable trajectories and
the outcomes that differentiate the classes. For methodological details on
the Bootstrapped Likelihood Ratio Test, see Nylund et al. (2007)
<doi:10.1080/10705510701575396>. For robust clustering methods, see
Garcia-Escudero et al. (2010) <doi:10.1007/s11634-010-0064-5>. For BCH
auxiliary variable analysis, see Bolck et al. (2004)
<doi:10.1093/pan/mph001>.

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
