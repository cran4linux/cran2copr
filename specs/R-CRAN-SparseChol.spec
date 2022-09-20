%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SparseChol
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Sparse Cholesky LDL Decomposition of Symmetric Matrices

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-Matrix >= 1.3.4
BuildRequires:    R-CRAN-Rcpp >= 1.0.7
Requires:         R-CRAN-Matrix >= 1.3.4
Requires:         R-CRAN-Rcpp >= 1.0.7

%description
'C++' implementation of sparse LDL decomposition of symmetric matrices and
solvers described by Timothy A. Davis (2016)
<https://fossies.org/linux/SuiteSparse/LDL/Doc/ldl_userguide.pdf>.
Provides the header file 'SparseChol.h' that specifies the 'SparseChol'
class to implement sparse LDL decomposition in 'Rcpp' functions. A limited
set of 'R' functions that implement the method are also included.

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
