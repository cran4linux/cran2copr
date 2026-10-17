%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  zukomp
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Portable Byte Compression with a Pluggable Codec Registry

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildRequires:    R-utils 
Requires:         R-utils 

%description
Compresses and decompresses raw vectors through a single codec-neutral
interface backed by a runtime registry, so the set of available codecs is
discovered rather than fixed at compile time. The 'DEFLATE' family
('gzip', 'zlib', and headerless 'DEFLATE') is built in from vendored
'miniz' sources, requiring no system compression library. Decompression
enforces configurable output-size and expansion-ratio limits and reports
failures through structured conditions. A registered C-callable interface
lets other packages drive the codecs from C and register codecs of their
own. The formats are specified in Deutsch (1996) <doi:10.17487/RFC1951>,
Deutsch and Gailly (1996) <doi:10.17487/RFC1950>, and Deutsch (1996)
<doi:10.17487/RFC1952>.

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
