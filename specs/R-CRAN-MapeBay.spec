%global __brp_check_rpaths %{nil}
%global packname  MapeBay
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Multivariate Analysis of Variance Panel, PERMANOVA and Bayesian

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
BuildRequires:    R-CRAN-MANOVA.RM 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinydashboardPlus 
BuildRequires:    R-CRAN-shinydashboard 
BuildRequires:    R-CRAN-MultBiplotR 
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-highcharter 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-nortest 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-reshape 
BuildRequires:    R-CRAN-shinycssloaders 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-MVN 
BuildRequires:    R-CRAN-heplots 
BuildRequires:    R-CRAN-mvnormtest 
BuildRequires:    R-CRAN-vegan 
BuildRequires:    R-CRAN-waiter 
BuildRequires:    R-CRAN-moments 
BuildRequires:    R-CRAN-rstantools
Requires:         R-CRAN-RcppParallel >= 5.0.1
Requires:         R-CRAN-rstan >= 2.18.1
Requires:         R-CRAN-rstantools >= 2.1.1
Requires:         R-CRAN-Rcpp >= 0.12.0
Requires:         R-methods 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-MANOVA.RM 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinydashboardPlus 
Requires:         R-CRAN-shinydashboard 
Requires:         R-CRAN-MultBiplotR 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-car 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-highcharter 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-nortest 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-reshape 
Requires:         R-CRAN-shinycssloaders 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-MVN 
Requires:         R-CRAN-heplots 
Requires:         R-CRAN-mvnormtest 
Requires:         R-CRAN-vegan 
Requires:         R-CRAN-waiter 
Requires:         R-CRAN-moments 
Requires:         R-CRAN-rstantools

%description
It covers approaches to multivariate analysis of variance, PERMANOVA and a
Bayesian analysis, presenting an assumption test section together with a
decision diagram that will allow selecting the appropriate technique for
the analysis. The presentation of results is through an interactive panel,
in which you can view automatic conclusions based on the tests, dynamic
graphics through 'Highchart', also the package uses 'Stan' for Bayesian
analysis.

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
