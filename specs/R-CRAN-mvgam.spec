%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mvgam
%global packver   1.1.51
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.51
Release:          1%{?dist}%{?buildtag}
Summary:          Multivariate (Dynamic) Generalized Additive Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildRequires:    R-CRAN-tibble >= 3.0.0
BuildRequires:    R-CRAN-loo >= 2.3.1
BuildRequires:    R-CRAN-rstan >= 2.29.0
BuildRequires:    R-CRAN-brms >= 2.21.0
BuildRequires:    R-CRAN-rstantools >= 2.1.1
BuildRequires:    R-CRAN-ggplot2 >= 2.0.0
BuildRequires:    R-CRAN-mgcv >= 1.8.13
BuildRequires:    R-CRAN-bayesplot >= 1.5.0
BuildRequires:    R-CRAN-patchwork >= 1.2.0
BuildRequires:    R-CRAN-posterior >= 1.0.0
BuildRequires:    R-CRAN-insight >= 0.19.1
BuildRequires:    R-CRAN-marginaleffects >= 0.16.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-mvnfast 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-rstantools
Requires:         R-CRAN-tibble >= 3.0.0
Requires:         R-CRAN-loo >= 2.3.1
Requires:         R-CRAN-rstan >= 2.29.0
Requires:         R-CRAN-brms >= 2.21.0
Requires:         R-CRAN-rstantools >= 2.1.1
Requires:         R-CRAN-ggplot2 >= 2.0.0
Requires:         R-CRAN-mgcv >= 1.8.13
Requires:         R-CRAN-bayesplot >= 1.5.0
Requires:         R-CRAN-patchwork >= 1.2.0
Requires:         R-CRAN-posterior >= 1.0.0
Requires:         R-CRAN-insight >= 0.19.1
Requires:         R-CRAN-marginaleffects >= 0.16.0
Requires:         R-CRAN-Rcpp >= 0.12.0
Requires:         R-methods 
Requires:         R-CRAN-mvnfast 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-generics 
Requires:         R-CRAN-rstantools

%description
Fit Bayesian Dynamic Generalized Additive Models to multivariate
observations. Users can build nonlinear State-Space models that can
incorporate semiparametric effects in observation and process components,
using a wide range of observation families. Estimation is performed using
Markov Chain Monte Carlo with Hamiltonian Monte Carlo in the software
'Stan'. References: Clark & Wells (2023) <doi:10.1111/2041-210X.13974>.

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
