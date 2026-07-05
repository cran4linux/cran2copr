%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  attestix
%global packver   0.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.1
Release:          1%{?dist}%{?buildtag}
Summary:          Offline Verifier for Attestix Ed25519 Credentials and UCAN Delegations

License:          Apache License (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-sodium 
BuildRequires:    R-CRAN-openssl 
BuildRequires:    R-CRAN-stringi 
Requires:         R-CRAN-sodium 
Requires:         R-CRAN-openssl 
Requires:         R-CRAN-stringi 

%description
An offline verifier for verifiable credentials and delegation chains
issued by the Attestix Python core. Verifies Ed25519 (RFC 8032) signatures
over W3C Verifiable Credentials, decodes Ed25519 'did:key' identifiers,
and verifies UCAN delegation chains (EdDSA 'JWT's) including capability
attenuation, with no Python runtime required. Reproduces the Attestix
JCS-style JSON canonical form (a practical subset of RFC 8785 that
additionally applies 'NFC' Unicode normalization) byte-for-byte so that
signatures produced by the reference implementation verify here. Useful
for compliance, research and biostatistics users who work in R and need to
check AI-agent compliance credentials. See <https://attestix.io> for the
project and <https://attestix.io/spec/bundle/v1> for the bundle wire
format.

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
