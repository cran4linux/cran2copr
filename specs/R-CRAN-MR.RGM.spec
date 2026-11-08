%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MR.RGM
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Multivariable Bidirectional Mendelian Randomization

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-GIGrvg 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-GIGrvg 

%description
Fits multivariable bidirectional Mendelian randomization networks with
Bayesian directed cyclic graphical models (reciprocal graphical models;
Ni, Ji and Mueller (2018) <doi:10.1214/17-BA1087>), an earlier version of
which is described in Sarkar and Ni (2025)
<doi:10.1093/bioinformatics/btaf130>. The causal effects among the
responses, which may form directed cycles, are estimated with
spike-and-slab or threshold priors, and posterior probabilities of network
motifs are provided. With a known instrument-response map the instrument
effects obey the exclusion restrictions; with an unrestricted map they are
selected by a spike-and-slab prior, which allows invalid instruments
(horizontal pleiotropy). The input can be individual-level data, the
second-moment matrices of one sample, or marginal instrument-response
regressions, with optional measured covariates. The error covariance can
be diagonal, inverse-Wishart, or a stochastic search structure learning
prior (Wang (2015) <doi:10.1214/14-BA916>) whose inclusion indicators
describe unmeasured confounding among the responses. Inference is by
Markov chain Monte Carlo with exact Gibbs updates of the instrument
effects and adaptive random-walk Metropolis updates of the causal effects
(Roberts and Rosenthal (2009) <doi:10.1198/jcgs.2009.06134>); the fitting
function reports diagnostics of weak instruments, weak identification and
convergence.

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
