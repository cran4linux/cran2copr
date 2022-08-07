%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MatrixExtra
%global packver   0.1.11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.11
Release:          1%{?dist}%{?buildtag}
Summary:          Extra Methods for Sparse Matrices

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Matrix >= 1.3
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RhpcBLASctl 
BuildRequires:    R-CRAN-float 
Requires:         R-CRAN-Matrix >= 1.3
Requires:         R-methods 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-RhpcBLASctl 
Requires:         R-CRAN-float 

%description
Extends sparse matrix and vector classes from the 'Matrix' package by
providing: (a) Methods and operators that work natively on CSR formats
(compressed sparse row, a.k.a. 'RsparseMatrix') such as
slicing/sub-setting, assignment, rbind(), mathematical operators for CSR
and COO such as addition ("+") or sqrt(), and methods such as diag(); (b)
Multi-threaded matrix multiplication and cross-product for many <sparse,
dense> types, including the 'float32' type from 'float'; (c) Coercion
methods between pairs of classes which are not present in 'Matrix', such
as 'dgCMatrix' -> 'ngRMatrix', as well as convenience conversion
functions; (d) Utility functions for sparse matrices such as sorting the
indices or removing zero-valued entries; (e) Fast transposes that work by
outputting in the opposite storage format; (f) Faster replacements for
many 'Matrix' methods for all sparse types, such as slicing and
elementwise multiplication. (g) Convenience functions for sparse objects,
such as 'mapSparse' or a shorter 'show' method.

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
