%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  LCPA
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          A General Framework for Latent Classify and Profile Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.0
BuildRequires:    R-CRAN-reticulate 
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
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 1.0.0
Requires:         R-CRAN-reticulate 
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

%description
A unified latent class modeling framework that encompasses both latent
class analysis (LCA) and latent profile analysis (LPA), offering a
one-stop solution for latent class modeling. It implements
state-of-the-art parameter estimation methods, including the
expectation–maximization (EM) algorithm, neural network estimation (NNE;
requires users to have 'Python' and its dependent libraries installed on
their computer), and integration with 'Mplus' (requires users to have
'Mplus' installed on their computer). In addition, it provides commonly
used model fit indices such as the Akaike information criterion (AIC) and
Bayesian information criterion (BIC), as well as classification accuracy
measures such as entropy. The package also includes fully functional
likelihood ratio tests (LRT) and bootstrap likelihood ratio tests (BLRT)
to facilitate model comparison, along with bootstrap-based and observed
information matrix-based standard error estimation. Furthermore, it
supports the standard three-step approach for LCA, LPA, and latent
transition analysis (LTA) with covariates, enabling detailed covariate
analysis. Finally, it includes several user-friendly auxiliary functions
to enhance interactive usability.

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
