%global packname  credentials
%global packver   1.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.0
Release:          1%{?dist}
Summary:          Tools for Managing SSH and Git Credentials

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         git
BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-sys >= 2.1
BuildRequires:    R-CRAN-openssl >= 1.3
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-askpass 
Requires:         R-CRAN-sys >= 2.1
Requires:         R-CRAN-openssl >= 1.3
Requires:         R-CRAN-curl 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-askpass 

%description
Setup and retrieve HTTPS and SSH credentials for use with 'git' and other
services. For HTTPS remotes the package interfaces the 'git-credential'
utility which 'git' uses to store HTTP usernames and passwords. For SSH
remotes we provide convenient functions to find or generate appropriate
SSH keys. The package both helps the user to setup a local git
installation, and also provides a back-end for git/ssh client libraries to
authenticate with existing user credentials.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
