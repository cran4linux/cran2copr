%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gKRLS
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Generalized Kernel Regularized Least Squares

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-sandwich >= 2.4.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.6
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-mlr3 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-sandwich >= 2.4.0
Requires:         R-CRAN-Rcpp >= 1.0.6
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-mlr3 
Requires:         R-CRAN-R6 

%description
Kernel regularized least squares, also known as kernel ridge regression,
is a flexible machine learning method. This package implements this method
by providing a smooth term for use with 'mgcv' and uses random sketching
to facilitate scalable estimation on large datasets. It provides
additional functions for calculating marginal effects after estimation and
for use with ensembles ('SuperLearning'), double/debiased machine learning
('DoubleML'), and robust/clustered standard errors ('sandwich'). Chang and
Goplerud (2023) <arXiv:2209.14355> provide further details.

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
