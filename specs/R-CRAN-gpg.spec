%global packname  gpg
%global packver   1.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.2
Release:          3%{?dist}
Summary:          GNU Privacy Guard for R

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    gpgme-devel
BuildRequires:    haveged-devel
Requires:         gpgme
Requires:         haveged
BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-askpass 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-askpass 

%description
Bindings to GnuPG for working with OpenGPG (RFC4880) cryptographic
methods. Includes utilities for public key encryption, creating and
verifying digital signatures, and managing your local keyring. Note that
some functionality depends on the version of GnuPG that is installed on
the system. On Windows this package can be used together with 'GPG4Win'
which provides a GUI for managing keys and entering passphrases.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
