%global __brp_check_rpaths %{nil}
%global packname  keyring
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Access the System Credential Store from R

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    libsecret-devel
BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-askpass 
BuildRequires:    R-CRAN-openssl 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-sodium 
BuildRequires:    R-CRAN-yaml 
BuildRequires:    R-CRAN-filelock 
BuildRequires:    R-CRAN-rappdirs 
BuildRequires:    R-tools 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-askpass 
Requires:         R-CRAN-openssl 
Requires:         R-CRAN-R6 
Requires:         R-utils 
Requires:         R-CRAN-sodium 
Requires:         R-CRAN-yaml 
Requires:         R-CRAN-filelock 
Requires:         R-CRAN-rappdirs 
Requires:         R-tools 

%description
Platform independent 'API' to access the operating system's credential
store. Currently supports: 'Keychain' on 'macOS', Credential Store on
'Windows', the Secret Service 'API' on 'Linux', and a simple, platform
independent store implemented with environment variables. Additional
storage back-ends can be added easily.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
