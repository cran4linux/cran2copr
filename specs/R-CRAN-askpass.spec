%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  askpass
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Password Entry Utilities for R, Git, and SSH

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
