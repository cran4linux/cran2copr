%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  survextrap
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Flexible Parametric Survival Modelling and Extrapolation

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-RcppParallel >= 5.0.1
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-rstan >= 2.26.0
BuildRequires:    R-CRAN-StanHeaders >= 2.26.0
BuildRequires:    R-CRAN-BH >= 1.66.0
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.3.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.0
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-loo 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-posterior 
BuildRequires:    R-CRAN-splines2 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-rstantools
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-rstan >= 2.26.0
Requires:         R-CRAN-Rcpp >= 0.12.0
Requires:         R-CRAN-survival 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-loo 
Requires:         R-methods 
Requires:         R-CRAN-posterior 
Requires:         R-CRAN-splines2 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-rstantools

%description
Survival analysis using a flexible Bayesian model for individual-level
right-censored data, optionally combined with aggregate data on counts of
survivors in different periods of time. An M-spline is used to describe
the hazard function, with a prior on the coefficients that controls
over-fitting. Proportional hazards or flexible non-proportional hazards
models can be used to relate survival to predictors. Additive hazards
(relative survival) models, waning treatment effects, and mixture cure
models are also supported. Priors can be customised and calibrated to
substantive beliefs. Posterior distributions are estimated using 'Stan',
and outputs are arranged in a tidy format. See Jackson (2023)
<doi:10.1186/s12874-023-02094-1>.

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
