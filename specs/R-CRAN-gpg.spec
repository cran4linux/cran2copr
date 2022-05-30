%global __brp_check_rpaths %{nil}
%global packname  gpg
%global packver   1.2.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.7
Release:          1%{?dist}%{?buildtag}
Summary:          GNU Privacy Guard for R

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    gpgme-devel
BuildRequires:    haveged-devel
BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-askpass 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-askpass 

%description
Bindings to GnuPG for working with OpenGPG (RFC4880) cryptographic
methods. Includes utilities for public key encryption, creating and
verifying digital signatures, and managing your local keyring. Some
functionality depends on the version of GnuPG that is installed on the
system. On Windows this package can be used together with 'GPG4Win' which
provides a GUI for managing keys and entering passphrases.

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
