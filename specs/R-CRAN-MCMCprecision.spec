%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MCMCprecision
%global packver   0.4.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.2
Release:          1%{?dist}%{?buildtag}
Summary:          Precision of Discrete Parameters in Transdimensional MCMC

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-parallel 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-combinat 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-RcppProgress 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-Rcpp 
Requires:         R-parallel 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-combinat 

%description
Estimates the precision of transdimensional Markov chain Monte Carlo
(MCMC) output, which is often used for Bayesian analysis of models with
different dimensionality (e.g., model selection). Transdimensional MCMC
(e.g., reversible jump MCMC) relies on sampling a discrete model-indicator
variable to estimate the posterior model probabilities. If only few
switches occur between the models, precision may be low and assessment
based on the assumption of independent samples misleading. Based on the
observed transition matrix of the indicator variable, the method of Heck,
Overstall, Gronau, & Wagenmakers (2019, Statistics & Computing, 29,
631-643) <doi:10.1007/s11222-018-9828-0> draws posterior samples of the
stationary distribution to (a) assess the uncertainty in the estimated
posterior model probabilities and (b) estimate the effective sample size
of the MCMC output.

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
