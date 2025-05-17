%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  seqHMM
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Mixture Hidden Markov Models for Social Sequence Data and Other Multivariate, Multichannel Categorical Time Series

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-TraMineR >= 2.2.7
BuildRequires:    R-CRAN-Rcpp >= 0.12.0
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggseqplot 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-gridBase 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-lhs 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-progressr 
BuildRequires:    R-CRAN-RcppHungarian 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-TraMineR >= 2.2.7
Requires:         R-CRAN-Rcpp >= 0.12.0
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-future.apply 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggseqplot 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-grid 
Requires:         R-CRAN-gridBase 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-lhs 
Requires:         R-CRAN-Matrix 
Requires:         R-methods 
Requires:         R-CRAN-nloptr 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-progressr 
Requires:         R-CRAN-RcppHungarian 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-utils 

%description
Designed for estimating variants of hidden (latent) Markov models (HMMs),
mixture HMMs, and non-homogeneous HMMs (NHMMs) for social sequence data
and other categorical time series. Special cases include
feedback-augmented NHMMs, Markov models without latent layer, mixture
Markov models, and latent class models. The package supports models for
one or multiple subjects with one or multiple parallel sequences
(channels). External covariates can be added to explain cluster membership
in mixture models as well as initial, transition and emission
probabilities in NHMMs. The package provides functions for evaluating and
comparing models, as well as functions for visualizing of multichannel
sequence data and HMMs. For NHMMs, methods for computing average causal
effects and marginal state and emission probabilities are available.
Models are estimated using maximum likelihood via the EM algorithm or
direct numerical maximization with analytical gradients. Documentation is
available via several vignettes, and Helske and Helske (2019,
<doi:10.18637/jss.v088.i03>). For methodology behind the NHMMs, see Helske
(2025, <doi:10.48550/arXiv.2503.16014>).

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
