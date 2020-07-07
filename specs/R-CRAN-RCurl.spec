%global packname  RCurl
%global packver   1.98-1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.98.1.2
Release:          3%{?dist}
Summary:          General Network (HTTP/FTP/...) Client Interface for R

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    make
BuildRequires:    libcurl-devel
BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-bitops 
Requires:         R-methods 
Requires:         R-CRAN-bitops 

%description
A wrapper for 'libcurl' <http://curl.haxx.se/libcurl/> Provides functions
to allow one to compose general HTTP requests and provides convenient
functions to fetch URIs, get & post forms, etc. and process the results
returned by the Web server. This provides a great deal of control over the
HTTP/FTP/... connection and the form of the request while providing a
higher-level interface than is available just using R socket connections.
Additionally, the underlying implementation is robust and extensive,
supporting FTP/FTPS/TFTP (uploads and downloads), SSL/HTTPS, telnet, dict,
ldap, and also supports cookies, redirects, authentication, etc.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CurlSSL
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/enums
%doc %{rlibdir}/%{packname}/etc
%doc %{rlibdir}/%{packname}/examples
%doc %{rlibdir}/%{packname}/HTTPErrors
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
