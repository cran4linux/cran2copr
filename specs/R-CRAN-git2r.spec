%global packname  git2r
%global packver   0.27.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.27.1
Release:          3%{?dist}%{?buildtag}
Summary:          Provides Access to Git Repositories

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    libgit2-devel
BuildRequires:    zlib-devel
BuildRequires:    openssl-devel
BuildRequires:    libssh2-devel
BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
Requires:         R-graphics 
Requires:         R-utils 

%description
Interface to the 'libgit2' library, which is a pure C implementation of
the 'Git' core methods. Provides access to 'Git' repositories to extract
data and running some basic 'Git' commands.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/AUTHORS
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/COPYING
%doc %{rlibdir}/%{packname}/COPYRIGHTS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
