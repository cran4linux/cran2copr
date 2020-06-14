%global packname  openssl
%global packver   1.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.1
Release:          2%{?dist}
Summary:          Toolkit for Encryption, Signatures and Certificates Based onOpenSSL

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz

BuildRequires:    openssl-devel >= 1.0.1
Requires:         openssl
BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-askpass 
Requires:         R-CRAN-askpass 

%description
Bindings to OpenSSL libssl and libcrypto, plus custom SSH key parsers.
Supports RSA, DSA and EC curves P-256, P-384, P-521, and curve25519.
Cryptographic signatures can either be created and verified manually or
via x509 certificates. AES can be used in cbc, ctr or gcm mode for
symmetric encryption; RSA for asymmetric (public key) encryption or EC for
Diffie Hellman. High-level envelope functions combine RSA and AES for
encrypting arbitrary sized data. Other utilities include key generators,
hash functions (md5, sha1, sha256, etc), base64 encoder, a secure random
number generator, and 'bignum' math methods for manually performing crypto
calculations on large multibyte integers.

%prep
%setup -q -c -n %{packname}


%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/cacert.pem
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
