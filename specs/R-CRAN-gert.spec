%global packname  gert
%global packver   0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3
Release:          3%{?dist}%{?buildtag}
Summary:          Simple Git Client for R

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    libgit2-devel >= 0.26
Requires:         libgit2
BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-openssl >= 1.4.1
BuildRequires:    R-CRAN-credentials >= 1.0
BuildRequires:    R-CRAN-askpass 
Requires:         R-CRAN-openssl >= 1.4.1
Requires:         R-CRAN-credentials >= 1.0
Requires:         R-CRAN-askpass 

%description
Simple git client based on 'libgit2' with user-friendly authentication and
support for both SSH and HTTPS remotes on all platforms. User credentials
are shared with command line 'git' through the git-credential store and
ssh keys stored on disk or ssh-agent. On Linux, a somewhat recent version
of 'libgit2' is required.

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
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
