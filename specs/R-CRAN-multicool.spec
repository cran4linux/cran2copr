%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  multicool
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Permutations of Multisets in Cool-Lex Order

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.11.2
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-gmp 
Requires:         R-CRAN-Rcpp >= 0.11.2
Requires:         R-methods 
Requires:         R-CRAN-gmp 

%description
A set of tools to permute multisets without loops or hash tables and to
generate integer partitions. The permutation functions are based on C code
from Aaron Williams. Cool-lex order is similar to colexicographical order.
The algorithm is described in Williams, A. Loopless Generation of Multiset
Permutations by Prefix Shifts. SODA 2009, Symposium on Discrete
Algorithms, New York, United States. The permutation code is distributed
without restrictions. Multinomial coefficients, Stirling numbers of the
second kind and Bell numbers are computed exactly using the 'gmp' package.
The package also generates the integer partitions of a positive, non-zero
integer n. The C++ code for this is based on Python code from Jerome
Kelleher, and the algorithm is described in Kelleher and O'Sullivan (2009)
<doi:10.48550/arXiv.0909.2331>. The C++ code and Python code are
distributed without conditions.

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
