%global __brp_check_rpaths %{nil}
%global packname  nonlinearTseries
%global packver   0.2.12
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.12
Release:          1%{?dist}%{?buildtag}
Summary:          Nonlinear Time Series Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.12
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-tseries 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.12.12
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-tseries 
Requires:         R-CRAN-zoo 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-lifecycle 

%description
Functions for nonlinear time series analysis. This package permits the
computation of the most-used nonlinear statistics/algorithms including
generalized correlation dimension, information dimension, largest Lyapunov
exponent, sample entropy and Recurrence Quantification Analysis (RQA),
among others. Basic routines for surrogate data testing are also included.
Part of this work was based on the book "Nonlinear time series analysis"
by Holger Kantz and Thomas Schreiber (ISBN: 9780521529020).

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
