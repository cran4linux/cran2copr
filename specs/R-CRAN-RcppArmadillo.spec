%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RcppArmadillo
%global packver   15.0.1-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          15.0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          'Rcpp' Integration for the 'Armadillo' Templated Linear Algebra Library

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.12
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-methods 
Requires:         R-CRAN-Rcpp >= 1.0.12
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-methods 

%description
'Armadillo' is a templated C++ linear algebra library aiming towards a
good balance between speed and ease of use. It provides high-level syntax
and functionality deliberately similar to Matlab. It is useful for
algorithm development directly in C++, or quick conversion of research
code into production environments. It provides efficient classes for
vectors, matrices and cubes where dense and sparse matrices are supported.
Integer, floating point and complex numbers are supported. A sophisticated
expression evaluator (based on template meta-programming) automatically
combines several operations to increase speed and efficiency. Dynamic
evaluation automatically chooses optimal code paths based on detected
matrix structures. Matrix decompositions are provided through integration
with LAPACK, or one of its high performance drop-in replacements (such as
'MKL' or 'OpenBLAS'). It can automatically use 'OpenMP' multi-threading
(parallelisation) to speed up computationally expensive operations.

The 'RcppArmadillo' package includes the header files from the 'Armadillo'
library; users do not need to install 'Armadillo' itself in order to use
'RcppArmadillo'. Starting from release 15.0.0, the minimum compilation
standard is C++14 so 'Armadillo' version 14.6.3 is included as a fallback
when an R package forces the C++11 standard. Package authors should set a
'#define' to select the 'current' version, or select the 'legacy' version
(also chosen as default) if they must. See 'GitHub issue #475' for
details.

Since release 7.800.0, 'Armadillo' is licensed under Apache License 2;
previous releases were under licensed as MPL 2.0 from version 3.800.0
onwards and LGPL-3 prior to that; 'RcppArmadillo' (the 'Rcpp'
bindings/bridge to Armadillo) is licensed under the GNU GPL version 2 or
later, as is the rest of 'Rcpp'.

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
