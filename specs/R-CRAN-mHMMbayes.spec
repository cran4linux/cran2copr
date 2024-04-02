%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mHMMbayes
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Multilevel Hidden Markov Models Using Bayesian Estimation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildRequires:    R-CRAN-MCMCpack 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-MCMCpack 
Requires:         R-CRAN-mvtnorm 
Requires:         R-stats 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-Rcpp 

%description
An implementation of the multilevel (also known as mixed or random
effects) hidden Markov model using Bayesian estimation in R. The
multilevel hidden Markov model (HMM) is a generalization of the well-known
hidden Markov model, for the latter see Rabiner (1989)
<doi:10.1109/5.18626>. The multilevel HMM is tailored to accommodate
(intense) longitudinal data of multiple individuals simultaneously, see
e.g., de Haan-Rietdijk et al. <doi:10.1080/00273171.2017.1370364>. Using a
multilevel framework, we allow for heterogeneity in the model parameters
(transition probability matrix and conditional distribution), while
estimating one overall HMM. The model can be fitted on multivariate data
with either a categorical, normal, or Poisson distribution, and include
individual level covariates (allowing for e.g., group comparisons on model
parameters). Parameters are estimated using Bayesian estimation utilizing
the forward-backward recursion within a hybrid Metropolis within Gibbs
sampler. Missing data (NA) in the dependent variables is accommodated
assuming MAR. The package also includes various visualization options, a
function to simulate data, and a function to obtain the most likely hidden
state sequence for each individual using the Viterbi algorithm.

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
