%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bayesdfa
%global packver   1.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Dynamic Factor Analysis (DFA) with 'Stan'

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-RcppParallel >= 5.0.1
BuildRequires:    R-CRAN-rstan >= 2.18.1
BuildRequires:    R-CRAN-StanHeaders >= 2.18.1
BuildRequires:    R-CRAN-rstantools >= 2.1.1
BuildRequires:    R-CRAN-loo >= 2.0.0
BuildRequires:    R-CRAN-mgcv >= 1.8.13
BuildRequires:    R-CRAN-BH >= 1.66.0
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.3.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.0
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-viridisLite 
BuildRequires:    R-CRAN-rstantools
Requires:         R-CRAN-rstan >= 2.18.1
Requires:         R-CRAN-rstantools >= 2.1.1
Requires:         R-CRAN-loo >= 2.0.0
Requires:         R-CRAN-mgcv >= 1.8.13
Requires:         R-CRAN-Rcpp >= 0.12.0
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-methods 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-rlang 
Requires:         R-splines 
Requires:         R-CRAN-viridisLite 
Requires:         R-CRAN-rstantools

%description
Implements Bayesian dynamic factor analysis with 'Stan'. Dynamic factor
analysis is a dimension reduction tool for multivariate time series.
'bayesdfa' extends conventional dynamic factor models in several ways.
First, extreme events may be estimated in the latent trend by modeling
process error with a student-t distribution. Second, alternative
constraints (including proportions are allowed). Third, the estimated
dynamic factors can be analyzed with hidden Markov models to evaluate
support for latent regimes.

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
