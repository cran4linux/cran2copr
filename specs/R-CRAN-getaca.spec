%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  getaca
%global packver   0.1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.6
Release:          1%{?dist}%{?buildtag}
Summary:          Reproducible External Data Dependencies

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-curl >= 5.0.0
BuildRequires:    R-stats 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-curl >= 5.0.0
Requires:         R-stats 
Requires:         R-tools 
Requires:         R-utils 

%description
Declares, retrieves, verifies, tracks and actively manages external data
dependencies too large or too fast-moving to ship inside a package.
Resources are identified by package, name and version, pinned to a Secure
Hash Algorithm (SHA-256) checksum, and resolved through an explicit policy
so that the same installed package always resolves the same bytes. A
registry served from a remote host may be signed with Ed25519 and verified
against a key the declaring package ships, so the declaration and the key
that vouches for it arrive by different routes. Hashing follows National
Institute of Standards and Technology (2015) "Secure Hash Standard"
<doi:10.6028/NIST.FIPS.180-4>; signing follows Bernstein, Duif, Lange,
Schwabe and Yang (2012) "High-Speed High-Security Signatures"
<doi:10.1007/s13389-012-0027-1> and Josefsson and Liusvaara (2017)
"Edwards-Curve Digital Signature Algorithm (EdDSA)"
<doi:10.17487/RFC8032>. Designed for reproducible offline use and graceful
behaviour during package checks.

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
