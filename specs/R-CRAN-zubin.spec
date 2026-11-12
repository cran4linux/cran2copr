%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  zubin
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Read and Write Structured Binary Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildRequires:    R-CRAN-zufast >= 0.1.0

%description
Describe a fixed binary record once, as a layout, and read or write
millions of them in one vectorised call: integers from 8 to 128 bits, the
half, single and double precision floats of the IEEE 754 (Institute of
Electrical and Electronics Engineers) standard, 'bfloat16' (brain floating
point), complex numbers, booleans, fixed bytes and fixed strings, padding,
arrays and 'C' struct alignment, in either byte order. Typed codecs
convert whole vectors to and from bytes at every width and byte order,
refusing rather than rounding a value that does not fit, and a growable
byte builder with a hard cap appends without quadratic copying. The same
buffer, cursor, typed reads and writes and layout kernels are a
header-only 'C' library that other packages use through 'LinkingTo' alone.

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
