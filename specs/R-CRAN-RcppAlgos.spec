%global packname  RcppAlgos
%global packver   2.4.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.4.3
Release:          1%{?dist}%{?buildtag}
Summary:          High Performance Tools for Combinatorics and Computational Mathematics

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    gmp-devel >= 4.2.3
BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-gmp 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RcppThread 
Requires:         R-CRAN-gmp 
Requires:         R-CRAN-Rcpp 
Requires:         R-methods 

%description
Provides optimized functions and flexible combinatorial iterators
implemented in C++ with 'Rcpp' for solving problems in combinatorics and
computational mathematics. Utilizes parallel programming via 'RcppThread'
for maximal performance. Also makes use of the RMatrix class from the
'RcppParallel' library. There are combination/permutation functions with
constraint parameters that allow for generation of all results of a vector
meeting specific criteria (e.g. generating integer partitions/compositions
or finding all combinations such that the sum is between two bounds).
Capable of generating specific combinations/permutations (e.g. retrieve
only the nth lexicographical result) which sets up nicely for
parallelization as well as random sampling. Gmp support permits
exploration where the total number of results is large (e.g.
comboSample(10000, 500, n = 4)). Additionally, there are several high
performance number theoretic functions that are useful for problems common
in computational mathematics. Some of these functions make use of the fast
integer division library 'libdivide'. The primeSieve function is based on
the segmented sieve of Eratosthenes implementation by Kim Walisch. It is
also efficient for large numbers by using the cache friendly improvements
originally developed by Tomás Oliveira. Finally, there is a prime counting
function that implements Legendre's formula based on the work of Kim
Walisch.

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
