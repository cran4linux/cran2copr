%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  growfunctions
%global packver   0.16
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.16
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Non-Parametric Dependent Models for Time-Indexed Functional Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.2
Requires:         R-core >= 3.2.2
BuildRequires:    R-CRAN-spam >= 2.7.0
BuildRequires:    R-CRAN-reshape2 >= 1.2.2
BuildRequires:    R-CRAN-ggplot2 >= 1.0.1
BuildRequires:    R-CRAN-RcppArmadillo >= 0.8.400.0.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.16
Requires:         R-CRAN-spam >= 2.7.0
Requires:         R-CRAN-reshape2 >= 1.2.2
Requires:         R-CRAN-ggplot2 >= 1.0.1
Requires:         R-CRAN-Rcpp >= 0.12.16

%description
Estimates a collection of time-indexed functions under either of Gaussian
process (GP) or intrinsic Gaussian Markov random field (iGMRF) prior
formulations where a Dirichlet process mixture allows sub-groupings of the
functions to share the same covariance or precision parameters.  The GP
and iGMRF formulations both support any number of additive covariance or
precision terms, respectively, expressing either or both of multiple trend
and seasonality.

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
