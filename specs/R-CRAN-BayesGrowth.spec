%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BayesGrowth
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Estimate Fish Growth Using MCMC Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-RcppParallel >= 5.0.1
BuildRequires:    R-CRAN-rstantools >= 2.3.1.1
BuildRequires:    R-CRAN-rstan >= 2.18.1
BuildRequires:    R-CRAN-StanHeaders >= 2.18.0
BuildRequires:    R-CRAN-BH >= 1.66.0
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.3.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.0
BuildRequires:    R-CRAN-AquaticLifeHistory 
BuildRequires:    R-CRAN-bayesplot 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-loo 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidybayes 
BuildRequires:    R-CRAN-rstantools
Requires:         R-CRAN-RcppParallel >= 5.0.1
Requires:         R-CRAN-rstantools >= 2.3.1.1
Requires:         R-CRAN-rstan >= 2.18.1
Requires:         R-CRAN-Rcpp >= 0.12.0
Requires:         R-CRAN-AquaticLifeHistory 
Requires:         R-CRAN-bayesplot 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-loo 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidybayes 
Requires:         R-CRAN-rstantools

%description
Estimate fish length-at-age models using MCMC analysis with 'rstan'
models. This package allows a multimodel approach to growth fitting to be
applied to length-at-age data and is supported by further analyses to
determine model selection and result presentation. The core methods of
this package are presented in Smart and Grammer (2021) "Modernising fish
and shark growth curves with Bayesian length-at-age models". PLOS ONE
16(2): e0246734 <doi:10.1371/journal.pone.0246734>.

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
