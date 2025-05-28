%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  libdeflate
%global packver   1.24-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.24.0
Release:          1%{?dist}%{?buildtag}
Summary:          DEFLATE Compression and Static Library

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0

%description
Whole-buffer DEFLATE-based compression and decompression of raw vectors
using the 'libdeflate' library (see
<https://github.com/ebiggers/libdeflate>). Provides the user with
additional control over the speed and the quality of DEFLATE compression
compared to the fixed level of compression offered in R's 'memCompress()'
function. Also provides the 'libdeflate' static library and 'C' headers
along with a 'CMake' target and 'package‑config' file that ease linking of
'libdeflate' in packages that compile and statically link bundled
libraries using 'CMake'.

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
