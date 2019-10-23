%global packname  parallelDist
%global packver   0.2.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.4
Release:          1%{?dist}
Summary:          Parallel Distance Matrix Computation using Multiple Threads

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildRequires:    R-CRAN-RcppParallel >= 4.3.20
BuildRequires:    R-CRAN-Rcpp >= 0.12.6
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-RcppParallel >= 4.3.20
Requires:         R-CRAN-Rcpp >= 0.12.6

%description
A fast parallelized alternative to R's native 'dist' function to calculate
distance matrices for continuous, binary, and multi-dimensional input
matrices, which supports a broad variety of 41 predefined distance
functions from the 'stats', 'proxy' and 'dtw' R packages, as well as user-
defined functions written in C++. For ease of use, the 'parDist' function
extends the signature of the 'dist' function and uses the same parameter
naming conventions as distance methods of existing R packages. The package
is mainly implemented in C++ and leverages the 'RcppParallel' package to
parallelize the distance computations with the help of the 'TinyThread'
library. Furthermore, the 'Armadillo' linear algebra library is used for
optimized matrix operations during distance calculations. The curiously
recurring template pattern (CRTP) technique is applied to avoid virtual
functions, which improves the Dynamic Time Warping calculations while the
implementation stays flexible enough to support different DTW step
patterns and normalization methods.

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
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
