%global __brp_check_rpaths %{nil}
%global packname  askpass
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Safe Password Entry for R, Git, and SSH

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz

BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-sys >= 2.1
Requires:         R-CRAN-sys >= 2.1

%description
Cross-platform utilities for prompting the user for credentials or a
passphrase, for example to authenticate with a server or read a protected
key. Includes native programs for MacOS and Windows, hence no 'tcltk' is
required. Password entry can be invoked in two different ways: directly
from R via the askpass() function, or indirectly as password-entry
back-end for 'ssh-agent' or 'git-credential' via the SSH_ASKPASS and
GIT_ASKPASS environment variables. Thereby the user can be prompted for
credentials or a passphrase if needed when R calls out to git or ssh.

%prep
%setup -q -c -n %{packname}
rm -f %{packname}/inst/mac*

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
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
