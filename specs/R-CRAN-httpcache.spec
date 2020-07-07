%global packname  httpcache
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          3%{?dist}
Summary:          Query Cache for HTTP Clients

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-httr >= 1.0.0
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-utils 
Requires:         R-CRAN-httr >= 1.0.0
Requires:         R-CRAN-digest 
Requires:         R-utils 

%description
In order to improve performance for HTTP API clients, 'httpcache' provides
simple tools for caching and invalidating cache. It includes the HTTP verb
functions GET, PUT, PATCH, POST, and DELETE, which are drop-in
replacements for those in the 'httr' package. These functions are
cache-aware and provide default settings for cache invalidation suitable
for RESTful APIs; the package also enables custom cache-management
strategies. Finally, 'httpcache' includes a basic logging framework to
facilitate the measurement of HTTP request time and cache performance.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
