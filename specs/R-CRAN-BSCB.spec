%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BSCB
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Simultaneous Credible Bands for Polynomial Regression

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-OptimalDesign 
BuildRequires:    R-CRAN-instantiate 
BuildRequires:    R-CRAN-posterior 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-OptimalDesign 
Requires:         R-CRAN-instantiate 
Requires:         R-CRAN-posterior 

%description
Provides functions to construct two-sided Bayesian simultaneous credible
bands (BSCBs) for the regression curve in univariate polynomial regression
over a finite covariate interval. Six methods are implemented, including
Normal-Gamma conjugate priors (with empirical Bayes, unit-information, and
g-prior hyperparameter specifications), non-conjugate priors fitted via
Hamiltonian Monte Carlo (HMC) using 'cmdstanr', and a non-informative
independent Jeffreys prior approach. Also includes functions for computing
the empirical simultaneous coverage rate (ESCR) and posterior simultaneous
coverage probability (PSCP), enabling performance comparison across
methods. The methodology is described in: Yang, F., Han, Y., Liu, W., &
Hall, I. (2026). "Bayesian simultaneous credible bands for polynomial
regression" <doi:10.48550/arXiv.2606.28015>.

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
