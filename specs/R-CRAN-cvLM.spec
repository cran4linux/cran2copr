%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cvLM
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Cross-Validation for Linear and Ridge Regression Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-RcppParallel >= 5.1.8
BuildRequires:    R-CRAN-Rcpp >= 1.0.13
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-RcppParallel >= 5.1.8
Requires:         R-CRAN-Rcpp >= 1.0.13
Requires:         R-stats 

%description
Implements cross-validation methods for linear and ridge regression
models. The package provides grid-based selection of the ridge penalty
parameter using Singular Value Decomposition (SVD) and supports K-fold
cross-validation, Leave-One-Out Cross-Validation (LOOCV), and Generalized
Cross-Validation (GCV). Computations are implemented in C++ via
'RcppArmadillo' with optional parallelization using 'RcppParallel'. The
methods are suitable for high-dimensional settings where the number of
predictors exceeds the number of observations.

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
