%global packname  gdns
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}
Summary:          Tools to Work with Google's 'DNS-over-HTTPS' ('DoH') 'API'

License:          AGPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-stringi 
Requires:         R-CRAN-httr 
Requires:         R-stats 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-stringi 

%description
To address the problem of insecurity of 'UDP'-based 'DNS' requests,
'Google Public DNS' offers 'DNS' resolution over an encrypted 'HTTPS'
connection. 'DNS-over-HTTPS' greatly enhances privacy and security between
a client and a recursive resolver, and complements 'DNSSEC' to provide
end-to-end authenticated 'DNS' lookups. Functions that enable querying
individual requests that bulk requests that return detailed responses and
bulk requests are both provided. Support for reverse lookups is also
provided. See
<https://developers.google.com/speed/public-dns/docs/dns-over-https> for
more information.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
