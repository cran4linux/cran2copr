%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cyclotomic
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          The Field of Cyclotomic Numbers

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-intmap 
BuildRequires:    R-CRAN-gmp 
BuildRequires:    R-CRAN-maybe 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-primes 
BuildRequires:    R-CRAN-VeryLargeIntegers 
Requires:         R-CRAN-intmap 
Requires:         R-CRAN-gmp 
Requires:         R-CRAN-maybe 
Requires:         R-methods 
Requires:         R-CRAN-primes 
Requires:         R-CRAN-VeryLargeIntegers 

%description
The cyclotomic numbers are complex numbers that can be thought of as the
rational numbers extended with the roots of unity. They are represented
exactly, enabling exact computations. They contain the Gaussian rationals
(complex numbers with rational real and imaginary parts) as well as the
square roots of all rational numbers. They also contain the sine and
cosine of all rational multiples of pi. The algorithms implemented in this
package are taken from the 'Haskell' package 'cyclotomic', whose
algorithms are adapted from code by Martin Schoenert and Thomas Breuer in
the 'GAP' project (<https://www.gap-system.org/>). Cyclotomic numbers have
applications in number theory, algebraic geometry, algebraic number
theory, coding theory, and in the theory of graphs and combinatorics. They
have connections to the theory of modular functions and modular curves.

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
