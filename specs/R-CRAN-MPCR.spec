%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MPCR
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Multi- And Mixed-Precision Computations

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.9
BuildRequires:    R-methods 
Requires:         R-CRAN-Rcpp >= 1.0.9
Requires:         R-methods 

%description
Designed for multi- and mixed-precision computations, accommodating 64-bit
and 32-bit data structures. This flexibility enables fast execution across
various applications. The package enhances performance by optimizing
operations in both precision levels, which is achieved by integrating with
high-speed 'BLAS' and 'LAPACK' libraries like 'MKL' and 'OpenBLAS'.
Including a 32-bit option caters to applications where high precision is
unnecessary, accelerating computational processes whenever feasible. The
package also provides support for tile-based algorithms in three linear
algebra operations: CHOL(), TRSM(), and GEMM(). The tile-based algorithm
splits the matrix into smaller tiles, facilitating parallelization through
a predefined Directed Acyclic Graph (DAG) for each operation. Enabling
'OpenMP' enhances the efficiency of these operations, leveraging
multi-core parallelism. In this case, 'MPCR' facilitates mixed-precision
execution by permitting varying precision levels for different tiles. This
approach is advantageous in numerous applications, as it maintains the
accuracy of the application while accelerating execution in scenarios
where single-precision alone does not significantly affect the accuracy of
the application.

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
