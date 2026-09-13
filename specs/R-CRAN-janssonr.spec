%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  janssonr
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Strict JSON Encoding and Decoding via the 'Jansson' C Library

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.4.0
Requires:         R-core >= 4.4.0

%description
An R-safe profile of RFC 8259 JSON: parsing and generation backed by the
'Jansson' C library, linked as a system library where one is available and
compiled from the bundled sources otherwise. The parser rejects, with
classed conditions carrying line, column, and byte position: malformed or
truncated input, trailing content, duplicate object keys at any depth,
invalid UTF-8, escapes encoding a null character, reals overflowing
double, and integer literals whose magnitude exceeds 2^53, the range
within which a double represents every integer exactly. Number literals
with a fraction or exponent convert by ordinary correctly rounded IEEE 754
double conversion. Objects decode to named lists in key order, arrays to
unnamed lists, and scalars to length-one vectors. The encoder maps named
lists to objects in insertion order, unnamed lists to arrays, guarantees
that every finite double, signed zero included, round-trips to the exact
same value (whole-number doubles are written as integers), and refuses
values with no faithful JSON representation (NA, NaN, infinities, named
atomic vectors, classed objects) instead of guessing. No R package
dependencies.

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
