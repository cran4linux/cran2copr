%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  conquer
%global packver   1.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.2
Release:          1%{?dist}%{?buildtag}
Summary:          Convolution-Type Smoothed Quantile Regression

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.3
BuildRequires:    R-CRAN-RcppArmadillo >= 0.9.850.1.0
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-stats 
Requires:         R-CRAN-Rcpp >= 1.0.3
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-matrixStats 
Requires:         R-stats 

%description
Estimation and inference for conditional linear quantile regression models
using a convolution smoothed approach. In the low-dimensional setting,
efficient gradient-based methods are employed for fitting both a single
model and a regression process over a quantile range. Normal-based and
(multiplier) bootstrap confidence intervals for all slope coefficients are
constructed. In high dimensions, the conquer method is complemented with
flexible types of penalties (Lasso, elastic-net, group lasso, sparse group
lasso, scad and mcp) to deal with complex low-dimensional structures.

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
