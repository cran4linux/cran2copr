%global packname  FLSSS
%global packver   8.5.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          8.5.6
Release:          2%{?dist}
Summary:          Mining Rigs for Specialized Subset Sum, Multi-Subset Sum,Multidimensional Subset Sum, Multidimensional Knapsack,Generalized Assignment Problems

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    make
BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.12.13
BuildRequires:    R-CRAN-RcppParallel 
Requires:         R-CRAN-Rcpp >= 0.12.13
Requires:         R-CRAN-RcppParallel 

%description
Specialized solvers for combinatorial optimization problems in the Subset
Sum family. These solvers differ from the mainstream in the options of (i)
restricting subset size, (ii) bounding subset elements, (iii) mining
real-value sets with predefined subset sum errors, and (iv) finding one or
more subsets in limited time. A novel algorithm for mining the
one-dimensional Subset Sum induced algorithms for the multi-Subset Sum and
the multidimensional Subset Sum. The latter decomposes the problem in a
novel approach, and the multi-threaded framework offers exact algorithms
to the multidimensional Knapsack and the Generalized Assignment problems.
Package updates include (a) renewed implementation of the multi-Subset
Sum, multidimensional Knapsack and Generalized Assignment solvers; (b)
availability of bounding solution space in the multidimensional Subset
Sum; (c) fundamental data structure and architectural changes for enhanced
cache locality and better chance of SIMD vectorization; (d) an option of
mapping real-domain problems to the integer domain with user-controlled
precision loss, and those integers are further zipped non-uniformly in
64-bit buffers. Arithmetic on compressed integers is done by
bit-manipulation and the design has virtually zero speed lag relative to
normal integers arithmetic. The consequent reduction in dimensionality may
yield substantial acceleration. Compilation with g++ '-Ofast' is
recommended. See package vignette (<arXiv:1612.04484v3>) for details.
Functions prefixed with 'aux' (auxiliary) are or will be implementations
of existing foundational or cutting-edge algorithms for solving
optimization problems of interest.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
