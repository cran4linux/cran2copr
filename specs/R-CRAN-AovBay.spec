%global __brp_check_rpaths %{nil}
%global packname  AovBay
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Classic, Nonparametric and Bayesian One-Way Analysis of Variance Panel

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-RcppParallel >= 5.0.1
BuildRequires:    R-CRAN-rstan >= 2.18.1
BuildRequires:    R-CRAN-StanHeaders >= 2.18.0
BuildRequires:    R-CRAN-rstantools >= 2.1.1
BuildRequires:    R-CRAN-BH >= 1.66.0
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.3.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinydashboardPlus 
BuildRequires:    R-CRAN-shinydashboard 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-BayesFactor 
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-highcharter 
BuildRequires:    R-CRAN-moments 
BuildRequires:    R-CRAN-reshape 
BuildRequires:    R-CRAN-nortest 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-shinycssloaders 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-waiter 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-rstantools
Requires:         R-CRAN-RcppParallel >= 5.0.1
Requires:         R-CRAN-rstan >= 2.18.1
Requires:         R-CRAN-rstantools >= 2.1.1
Requires:         R-CRAN-Rcpp >= 0.12.0
Requires:         R-methods 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinydashboardPlus 
Requires:         R-CRAN-shinydashboard 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-BayesFactor 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-car 
Requires:         R-CRAN-highcharter 
Requires:         R-CRAN-moments 
Requires:         R-CRAN-reshape 
Requires:         R-CRAN-nortest 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-shinycssloaders 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-waiter 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-rstantools

%description
It covers various approaches to analysis of variance, provides an
assumption testing section in order to provide a decision diagram that
allows selecting the most appropriate technique. It provides the classical
analysis of variance, the nonparametric equivalent of Kruskal Wallis, and
the Bayesian approach. These results are shown in an interactive shiny
panel, which allows modifying the arguments of the tests, contains
interactive graphics and presents automatic conclusions depending on the
tests in order to contribute to the interpretation of these analyzes.
'AovBay' uses 'Stan' and 'FactorBayes' for Bayesian analysis and
'Highcharts' for interactive charts.

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
