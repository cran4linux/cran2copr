%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bayes4psy
%global packver   1.2.13
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.13
Release:          1%{?dist}%{?buildtag}
Summary:          User Friendly Bayesian Data Analysis for Psychology

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-methods >= 4.0.0
BuildRequires:    R-stats >= 4.0.0
BuildRequires:    R-CRAN-ggplot2 >= 3.3.2
BuildRequires:    R-CRAN-rstan >= 2.26.0
BuildRequires:    R-CRAN-StanHeaders >= 2.26.0
BuildRequires:    R-CRAN-rstantools >= 2.1.1
BuildRequires:    R-CRAN-BH >= 1.72.0.3
BuildRequires:    R-CRAN-mcmcse >= 1.4.1
BuildRequires:    R-CRAN-cowplot >= 1.1.0
BuildRequires:    R-CRAN-emg >= 1.0.9
BuildRequires:    R-CRAN-Rcpp >= 1.0.5
BuildRequires:    R-CRAN-dplyr >= 1.0.2
BuildRequires:    R-CRAN-metRology >= 0.9.28.1
BuildRequires:    R-CRAN-reshape >= 0.8.8
BuildRequires:    R-CRAN-circular >= 0.4.93
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.7.0
BuildRequires:    R-CRAN-RcppParallel 
BuildRequires:    R-CRAN-rstantools
Requires:         R-methods >= 4.0.0
Requires:         R-stats >= 4.0.0
Requires:         R-CRAN-ggplot2 >= 3.3.2
Requires:         R-CRAN-rstan >= 2.26.0
Requires:         R-CRAN-rstantools >= 2.1.1
Requires:         R-CRAN-mcmcse >= 1.4.1
Requires:         R-CRAN-cowplot >= 1.1.0
Requires:         R-CRAN-emg >= 1.0.9
Requires:         R-CRAN-Rcpp >= 1.0.5
Requires:         R-CRAN-dplyr >= 1.0.2
Requires:         R-CRAN-metRology >= 0.9.28.1
Requires:         R-CRAN-reshape >= 0.8.8
Requires:         R-CRAN-circular >= 0.4.93
Requires:         R-CRAN-RcppParallel 
Requires:         R-CRAN-rstantools

%description
Contains several Bayesian models for data analysis of psychological tests.
A user friendly interface for these models should enable students and
researchers to perform professional level Bayesian data analysis without
advanced knowledge in programming and Bayesian statistics. This package is
based on the Stan platform (Carpenter et el. 2017
<doi:10.18637/jss.v076.i01>).

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
