%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  seqHMM
%global packver   1.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.3
Release:          1%{?dist}%{?buildtag}
Summary:          Mixture Hidden Markov Models for Social Sequence Data and Other Multivariate, Multichannel Categorical Time Series

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-TraMineR >= 1.8.8
BuildRequires:    R-CRAN-Rcpp >= 0.11.3
BuildRequires:    R-CRAN-gridBase 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-grid 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-TraMineR >= 1.8.8
Requires:         R-CRAN-Rcpp >= 0.11.3
Requires:         R-CRAN-gridBase 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-nloptr 
Requires:         R-CRAN-numDeriv 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-grid 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 

%description
Designed for fitting hidden (latent) Markov models and mixture hidden
Markov models for social sequence data and other categorical time series.
Also some more restricted versions of these type of models are available:
Markov models, mixture Markov models, and latent class models. The package
supports models for one or multiple subjects with one or multiple parallel
sequences (channels). External covariates can be added to explain cluster
membership in mixture models. The package provides functions for
evaluating and comparing models, as well as functions for visualizing of
multichannel sequence data and hidden Markov models. Models are estimated
using maximum likelihood via the EM algorithm and/or direct numerical
maximization with analytical gradients. All main algorithms are written in
C++ with support for parallel computation. Documentation is available via
several vignettes in this page, and the paper by Helske and Helske (2019,
<doi:10.18637/jss.v088.i03>).

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
