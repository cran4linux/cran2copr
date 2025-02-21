%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  flint
%global packver   0.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Fast Library for Number Theory

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3
Requires:         R-core >= 4.3
BuildRequires:    R-methods 
BuildRequires:    R-stats 
Requires:         R-methods 
Requires:         R-stats 

%description
An R interface to 'FLINT' <https://flintlib.org/>, a C library for number
theory.  'FLINT' extends GNU 'MPFR' <https://www.mpfr.org/> and GNU 'MP'
<https://gmplib.org/> with support for arithmetic in standard rings (the
integers, the integers modulo n, the rational, p-adic, real, and complex
numbers) as well as vectors, matrices, polynomials, and power series over
rings.  'FLINT' implements midpoint-radius interval arithmetic, also known
as ball arithmetic, in the real and complex numbers, enabling computation
in arbitrary precision with rigorous propagation of errors; see Johansson
(2017) <doi:10.1109/TC.2017.2690633>.  Finally, 'FLINT' provides ball
arithmetic implementations of many special mathematical functions, with
high coverage of reference works such as the NIST Digital Library of
Mathematical Functions <https://dlmf.nist.gov/>.  The R interface defines
S4 classes, generic functions, and methods for representation and basic
operations as well as plain R functions matching and vectorizing entry
points in the C library.

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
