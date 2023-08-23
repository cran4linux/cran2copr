%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ubms
%global packver   1.2.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.5
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Models for Data from Unmarked Animals using 'Stan'

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-RcppParallel >= 5.0.2
BuildRequires:    R-CRAN-rstan >= 2.18.1
BuildRequires:    R-CRAN-StanHeaders >= 2.18.0
BuildRequires:    R-CRAN-ggplot2 >= 2.0.0
BuildRequires:    R-CRAN-rstantools >= 2.0.0
BuildRequires:    R-CRAN-BH >= 1.66.0
BuildRequires:    R-CRAN-Matrix >= 1.5.0
BuildRequires:    R-CRAN-RcppArmadillo >= 0.9.300.2.0
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.3.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.0
BuildRequires:    R-CRAN-unmarked 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-loo 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-RSpectra 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-rstantools
Requires:         R-CRAN-rstan >= 2.18.1
Requires:         R-CRAN-ggplot2 >= 2.0.0
Requires:         R-CRAN-rstantools >= 2.0.0
Requires:         R-CRAN-Matrix >= 1.5.0
Requires:         R-CRAN-Rcpp >= 0.12.0
Requires:         R-CRAN-unmarked 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-loo 
Requires:         R-methods 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-RSpectra 
Requires:         R-stats 
Requires:         R-CRAN-rstantools

%description
Fit Bayesian hierarchical models of animal abundance and occurrence via
the 'rstan' package, the R interface to the 'Stan' C++ library. Supported
models include single-season occupancy, dynamic occupancy, and N-mixture
abundance models. Covariates on model parameters are specified using a
formula-based interface similar to package 'unmarked', while also allowing
for estimation of random slope and intercept terms. References: Carpenter
et al. (2017) <doi:10.18637/jss.v076.i01>; Fiske and Chandler (2011)
<doi:10.18637/jss.v043.i10>.

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
