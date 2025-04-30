%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  boral
%global packver   2.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Ordination and Regression AnaLysis

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-corpcor 
BuildRequires:    R-CRAN-fishMod 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-R2jags 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-stats 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-corpcor 
Requires:         R-CRAN-fishMod 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-R2jags 
Requires:         R-CRAN-reshape2 
Requires:         R-stats 

%description
Bayesian approaches for analyzing multivariate data in ecology. Estimation
is performed using Markov Chain Monte Carlo (MCMC) methods via Three. JAGS
types of models may be fitted: 1) With explanatory variables only, boral
fits independent column Generalized Linear Models (GLMs) to each column of
the response matrix; 2) With latent variables only, boral fits a purely
latent variable model for model-based unconstrained ordination; 3) With
explanatory and latent variables, boral fits correlated column GLMs with
latent variables to account for any residual correlation between the
columns of the response matrix.

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
