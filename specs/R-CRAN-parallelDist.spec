%global __brp_check_rpaths %{nil}
%global packname  parallelDist
%global packver   0.2.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.6
Release:          1%{?dist}%{?buildtag}
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
