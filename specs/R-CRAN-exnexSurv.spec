%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  exnexSurv
%global packver   1.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian EXNEX Models for Survival Analysis in Basket Trials

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-checkmate >= 2.1.0
BuildRequires:    R-CRAN-hardhat >= 1.4.0
BuildRequires:    R-CRAN-Rcpp >= 1.1.1
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-checkmate >= 2.1.0
Requires:         R-CRAN-hardhat >= 1.4.0
Requires:         R-CRAN-Rcpp >= 1.1.1

%description
Implements the Bayesian Exchangeable Non-Exchangeable (EXNEX) framework
for right-censored log-normal survival data in basket trials. Based on
'Rcpp' and 'RcppArmadillo', the package provides a fast Gibbs sampler
supporting EXNEX, complete pooling, and no pooling models to facilitate
methodological comparisons and simulation studies.

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
