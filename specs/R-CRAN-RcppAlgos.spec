%global packname  RcppAlgos
%global packver   2.3.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3.5
Release:          1%{?dist}
Summary:          High Performance Tools for Combinatorics and ComputationalMathematics

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    gmp-devel >= 4.2.3
Requires:         gmp
BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-gmp 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppThread 
Requires:         R-CRAN-gmp 
Requires:         R-CRAN-Rcpp 

%description
Provides optimized functions implemented in C++ with 'Rcpp' for solving
problems in combinatorics and computational mathematics. Utilizes parallel
programming via 'RcppThread' for maximal performance. Also makes use of
the RMatrix class from the 'RcppParallel' library. There are
combination/permutation functions with constraint parameters that allow
for generation of all combinations/permutations of a vector meeting
specific criteria (e.g. generating integer partitions/compositions or
finding all combinations such that the sum is between two bounds). Capable
of generating specific combinations/permutations (e.g. retrieve only the
nth lexicographical result) which sets up nicely for parallelization as
well as random sampling. Gmp support permits exploration where the total
number of results is large (e.g. comboSample(10000, 500, n = 4)).
Additionally, there are several high performance number theoretic
functions that are useful for problems common in computational
mathematics. Some of these functions make use of the fast integer division
library 'libdivide'. The primeSieve function is based on the segmented
sieve of Eratosthenes implementation by Kim Walisch. It is also efficient
for large numbers by using the cache friendly improvements originally
developed by Tomás Oliveira. Finally, there is a prime counting function
that implements Legendre's formula based on the work of Kim Walisch.

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/figures
%{rlibdir}/%{packname}/include
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
