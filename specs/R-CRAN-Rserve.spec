%global packname  Rserve
%global packver   1.7-3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7.3.1
Release:          3%{?dist}%{?buildtag}
Summary:          Binary R server

License:          GPL-2 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    make
BuildRequires:    R-devel >= 1.5.0
Requires:         R-core >= 1.5.0

%description
Rserve acts as a socket server (TCP/IP or local sockets) which allows
binary requests to be sent to R. Every connection has a separate workspace
and working directory. Client-side implementations are available for
popular languages such as C/C++ and Java, allowing any application to use
facilities of R without the need of linking to R code. Rserve supports
remote connection, user authentication and file transfer. A simple R
client is included in this package as well.

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
%doc %{rlibdir}/%{packname}/java
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
