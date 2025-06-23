%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  FLSSS
%global packver   9.2.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          9.2.8
Release:          1%{?dist}%{?buildtag}
Summary:          Mining Rigs for Problems in the Subset Sum Family

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.12.13
BuildRequires:    R-CRAN-RcppParallel 
Requires:         R-CRAN-Rcpp >= 0.12.13
Requires:         R-CRAN-RcppParallel 

%description
Specialized solvers for combinatorial optimization problems in the Subset
Sum family. The solvers differ from the mainstream in the options of (i)
restricting subset size, (ii) bounding subset elements, (iii) mining
real-value multisets with predefined subset sum errors, (iv) finding one
or more subsets in limited time. A novel algorithm for mining the
one-dimensional Subset Sum induced algorithms for the multi-Subset Sum and
the multidimensional Subset Sum. The multi-threaded framework for the
latter offers exact algorithms to the multidimensional Knapsack and the
Generalized Assignment problems. Historical updates include (a) renewed
implementation of the multi-Subset Sum, multidimensional Knapsack and
Generalized Assignment solvers; (b) availability of bounding solution
space in the multidimensional Subset Sum; (c) fundamental data structure
and architectural changes for enhanced cache locality and better chance of
SIMD vectorization; (d) option of mapping floating-point instance to
compressed 64-bit integer instance with user-controlled precision loss,
which could yield substantial speedup due to the dimension reduction and
efficient compressed integer arithmetic via bit-manipulations; (e)
distributed computing infrastructure for multidimensional subset sum; (f)
arbitrary-precision zero-margin-of-error multidimensional Subset Sum
accelerated by a simplified Bloom filter. The package contains a copy of
'xxHash' from <https://github.com/Cyan4973/xxHash>. Package vignette
(<doi:10.48550/arXiv.1612.04484>) detailed a few historical updates.
Functions prefixed with 'aux' (auxiliary) are independent implementations
of published algorithms for solving optimization problems less relevant to
Subset Sum.

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
