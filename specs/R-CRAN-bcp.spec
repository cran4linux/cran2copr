%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bcp
%global packver   4.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.0.4
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Analysis of Change Point Problems

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.11.0
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.11.0
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-grid 

%description
Provides an implementation of the product partition model described in
Barry and Hartigan (2019) <doi:10.2307/2290726> for the normal errors
change point problem using Markov Chain Monte Carlo (MCMC). It also
extends the methodology to regression models on a connected graph as
reported in Wang and Emerson (2015) <doi:10.48550/arXiv.1509.00817>,
allowing estimation of change point models with multivariate responses.
Parallel MCMC, previously available in 'bcp' v.3.0.0, is currently not
implemented.

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
