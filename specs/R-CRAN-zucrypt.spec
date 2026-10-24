%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  zucrypt
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Cryptography Without System Dependencies

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildRequires:    R-utils 
Requires:         R-utils 

%description
Cryptographic functions over raw vectors, including message digests of
in-memory data, files and connections, keyed-hash message authentication
codes (HMAC), Advanced Encryption Standard (AES) encryption, constant-time
comparison and hexadecimal encoding, backed by a bundled and pinned copy
of the 'Mbed TLS' project's cryptography library, 'TF-PSA-Crypto'
(<https://github.com/Mbed-TLS/TF-PSA-Crypto>). No system cryptographic
library, 'Java' or 'Python' is required at install or run time. Algorithm
names are matched exactly, and failures are reported as structured
conditions. The same primitives, and secure erasure of native buffers, are
published to other packages as a static archive and as a registered C
interface, so that a package can call them from C without going through R.

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
