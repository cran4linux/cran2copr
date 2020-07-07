%global packname  keyring
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          3%{?dist}
Summary:          Access the System Credential Store from R

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz

BuildRequires:    libsecret-devel
Requires:         libsecret
BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-getPass 
BuildRequires:    R-CRAN-openssl 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-sodium 
BuildRequires:    R-CRAN-yaml 
BuildRequires:    R-CRAN-filelock 
BuildRequires:    R-CRAN-rappdirs 
BuildRequires:    R-tools 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-getPass 
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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/development-notes.md
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
