%global packname  bigalgebra
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          'BLAS' and 'LAPACK' Routines for Native R Matrices and 'big.matrix' Objects

License:          LGPL-3 | Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-bigmemory >= 4.0.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-BH 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-bigmemory >= 4.0.0
Requires:         R-methods 

%description
Provides arithmetic functions for R matrix and 'big.matrix' objects as
well as functions for QR factorization, Cholesky factorization, General
eigenvalue, and Singular value decomposition (SVD). A method matrix
multiplication and an arithmetic method -for matrix addition, matrix
difference- allows for mixed type operation -a matrix class object and a
big.matrix class object- and pure type operation for two big.matrix class
objects.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
