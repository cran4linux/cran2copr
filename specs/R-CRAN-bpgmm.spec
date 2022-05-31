%global __brp_check_rpaths %{nil}
%global packname  bpgmm
%global packver   1.0.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.8
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Model Selection Approach for Parsimonious Gaussian Mixture Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-CRAN-MASS >= 7.3.51.1
BuildRequires:    R-CRAN-mclust >= 5.4.3
BuildRequires:    R-CRAN-fabMix >= 5.0
BuildRequires:    R-CRAN-gtools >= 3.8.1
BuildRequires:    R-methods >= 3.5.1
BuildRequires:    R-CRAN-label.switching >= 1.8
BuildRequires:    R-CRAN-mcmcse >= 1.3.2
BuildRequires:    R-CRAN-pgmm >= 1.2.3
BuildRequires:    R-CRAN-mvtnorm >= 1.0.10
BuildRequires:    R-CRAN-Rcpp >= 1.0.1
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-MASS >= 7.3.51.1
Requires:         R-CRAN-mclust >= 5.4.3
Requires:         R-CRAN-fabMix >= 5.0
Requires:         R-CRAN-gtools >= 3.8.1
Requires:         R-methods >= 3.5.1
Requires:         R-CRAN-label.switching >= 1.8
Requires:         R-CRAN-mcmcse >= 1.3.2
Requires:         R-CRAN-pgmm >= 1.2.3
Requires:         R-CRAN-mvtnorm >= 1.0.10
Requires:         R-CRAN-Rcpp >= 1.0.1

%description
Model-based clustering using Bayesian parsimonious Gaussian mixture
models. MCMC (Markov chain Monte Carlo) are used for parameter estimation.
The RJMCMC (Reversible-jump Markov chain Monte Carlo) is used for model
selection. GREEN et al. (1995) <doi:10.1093/biomet/82.4.711>.

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
