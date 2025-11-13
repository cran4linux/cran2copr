%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  digest
%global packver   0.6.38
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.38
Release:          1%{?dist}%{?buildtag}
Summary:          Create Compact Hash Digests of R Objects

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-utils 
Requires:         R-utils 

%description
Implementation of a function 'digest()' for the creation of hash digests
of arbitrary R objects (using the 'md5', 'sha-1', 'sha-256', 'crc32',
'xxhash', 'murmurhash', 'spookyhash', 'blake3', 'crc32c', 'xxh3_64', and
'xxh3_128' algorithms) permitting easy comparison of R language objects,
as well as functions such as 'hmac()' to create hash-based message
authentication code. Please note that this package is not meant to be
deployed for cryptographic purposes for which more comprehensive (and
widely tested) libraries such as 'OpenSSL' should be used.

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
