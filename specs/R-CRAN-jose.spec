%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  jose
%global packver   1.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          JavaScript Object Signing and Encryption

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-openssl >= 1.2.1
BuildRequires:    R-CRAN-jsonlite 
Requires:         R-CRAN-openssl >= 1.2.1
Requires:         R-CRAN-jsonlite 

%description
Read and write JSON Web Keys (JWK, rfc7517), generate and verify JSON Web
Signatures (JWS, rfc7515) and encode/decode JSON Web Tokens (JWT, rfc7519)
<https://datatracker.ietf.org/wg/jose/documents/>. These standards provide
modern signing and encryption formats that are natively supported by
browsers via the JavaScript WebCryptoAPI
<https://www.w3.org/TR/WebCryptoAPI/#jose>, and used by services like
OAuth 2.0, LetsEncrypt, and Github Apps.

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
