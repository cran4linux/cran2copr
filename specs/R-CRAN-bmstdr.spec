%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bmstdr
%global packver   0.8.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.2
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Modeling of Spatio-Temporal Data with R

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-rstan >= 2.18.1
BuildRequires:    R-CRAN-StanHeaders >= 2.18.0
BuildRequires:    R-CRAN-BH >= 1.66.0
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.3.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-spTimer 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-rstantools 
BuildRequires:    R-CRAN-spBayes 
BuildRequires:    R-CRAN-CARBayes 
BuildRequires:    R-CRAN-CARBayesST 
BuildRequires:    R-CRAN-spTDyn 
BuildRequires:    R-CRAN-MCMCpack 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-mnormt 
BuildRequires:    R-CRAN-inlabru 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-RcppParallel 
BuildRequires:    R-CRAN-rstantools
Requires:         R-CRAN-Rcpp >= 0.12.0
Requires:         R-methods 
Requires:         R-CRAN-spTimer 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-rstan >= 2.18.1
Requires:         R-CRAN-rstantools 
Requires:         R-CRAN-spBayes 
Requires:         R-CRAN-CARBayes 
Requires:         R-CRAN-CARBayesST 
Requires:         R-CRAN-spTDyn 
Requires:         R-CRAN-MCMCpack 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-mnormt 
Requires:         R-CRAN-inlabru 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-rstantools

%description
Fits, validates and compares a number of Bayesian models for spatial and
space time point referenced and areal unit data. Model fitting is done
using several packages: 'rstan', 'INLA', 'spBayes', 'spTimer', 'spTDyn',
'CARBayes' and 'CARBayesST'. Model comparison is performed using the DIC
and WAIC, and K-fold cross-validation where the user is free to select
their own subset of data rows for validation. Sahu (2022)
<doi:10.1201/9780429318443> describes the methods in detail.

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
