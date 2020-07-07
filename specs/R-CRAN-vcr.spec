%global packname  vcr
%global packver   0.5.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.4
Release:          3%{?dist}
Summary:          Record 'HTTP' Calls to Disk

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-crul >= 0.8.4
BuildRequires:    R-CRAN-webmockr >= 0.6.2
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-urltools 
BuildRequires:    R-CRAN-yaml 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-lazyeval 
BuildRequires:    R-CRAN-base64enc 
Requires:         R-CRAN-crul >= 0.8.4
Requires:         R-CRAN-webmockr >= 0.6.2
Requires:         R-CRAN-httr 
Requires:         R-CRAN-urltools 
Requires:         R-CRAN-yaml 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-lazyeval 
Requires:         R-CRAN-base64enc 

%description
Record test suite 'HTTP' requests and replays them during future runs. A
port of the Ruby gem of the same name (<https://github.com/vcr/vcr/>).
Works by hooking into the 'webmockr' R package for matching 'HTTP'
requests by various rules ('HTTP' method, 'URL', query parameters,
headers, body, etc.), and then caching real 'HTTP' responses on disk in
'cassettes'. Subsequent 'HTTP' requests matching any previous requests in
the same 'cassette' use a cached 'HTTP' response.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
