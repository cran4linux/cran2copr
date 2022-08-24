%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  multinomialLogitMix
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Clustering Multinomial Count Data under the Presence of Covariates

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 1.0.8.3
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-label.switching 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 1.0.8.3
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-label.switching 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-RColorBrewer 

%description
Methods for model-based clustering of multinomial counts under the
presence of covariates using mixtures of multinomial logit models, as
implemented in Papastamoulis (2022) <DOI:10.48550/arXiv.2207.13984>. These
models are estimated under a frequentist as well as a Bayesian setup using
the Expectation-Maximization algorithm and Markov chain Monte Carlo
sampling (MCMC), respectively. The (unknown) number of clusters is
selected according to the Integrated Completed Likelihood criterion (for
the frequentist model), and estimating the number of non-empty components
using overfitting mixture models after imposing suitable sparse prior
assumptions on the mixing proportions (in the Bayesian case), see Rousseau
and Mengersen (2011) <DOI:10.1111/j.1467-9868.2011.00781.x>. In the latter
case, various MCMC chains run in parallel and are allowed to switch
states. The final MCMC output is suitably post-processed in order to undo
label switching using the Equivalence Classes Representatives (ECR)
algorithm, as described in Papastamoulis (2016)
<DOI:10.18637/jss.v069.c01>.

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
