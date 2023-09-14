%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rstanarm
%global packver   2.26.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.26.1
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Applied Regression Modeling via Stan

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Recommends:       pandoc
BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-RcppParallel >= 5.0.1
BuildRequires:    R-CRAN-nlme >= 3.1.124
BuildRequires:    R-CRAN-survival >= 2.40.1
BuildRequires:    R-CRAN-shinystan >= 2.3.0
BuildRequires:    R-CRAN-rstan >= 2.26.1
BuildRequires:    R-CRAN-StanHeaders >= 2.21.0
BuildRequires:    R-CRAN-ggplot2 >= 2.2.1
BuildRequires:    R-CRAN-loo >= 2.1.0
BuildRequires:    R-CRAN-rstantools >= 2.1.0
BuildRequires:    R-CRAN-BH >= 1.72.0.2
BuildRequires:    R-CRAN-bayesplot >= 1.7.0
BuildRequires:    R-CRAN-Matrix >= 1.2.13
BuildRequires:    R-CRAN-lme4 >= 1.1.8
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.3.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-posterior 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-rstantools
Requires:         R-CRAN-RcppParallel >= 5.0.1
Requires:         R-CRAN-nlme >= 3.1.124
Requires:         R-CRAN-survival >= 2.40.1
Requires:         R-CRAN-shinystan >= 2.3.0
Requires:         R-CRAN-rstan >= 2.26.1
Requires:         R-CRAN-ggplot2 >= 2.2.1
Requires:         R-CRAN-loo >= 2.1.0
Requires:         R-CRAN-rstantools >= 2.1.0
Requires:         R-CRAN-bayesplot >= 1.7.0
Requires:         R-CRAN-Matrix >= 1.2.13
Requires:         R-CRAN-lme4 >= 1.1.8
Requires:         R-CRAN-Rcpp >= 0.12.0
Requires:         R-methods 
Requires:         R-CRAN-posterior 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-rstantools

%description
Estimates previously compiled regression models using the 'rstan' package,
which provides the R interface to the Stan C++ library for Bayesian
estimation. Users specify models via the customary R syntax with a formula
and data.frame plus some additional arguments for priors.

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
