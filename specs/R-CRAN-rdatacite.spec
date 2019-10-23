%global packname  rdatacite
%global packver   0.4.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.2
Release:          1%{?dist}
Summary:          'DataCite' Client for 'OAI-PMH' Methods and their Search API

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-solrium >= 1.0.0
BuildRequires:    R-CRAN-crul >= 0.7.4
BuildRequires:    R-CRAN-oai >= 0.2.2
BuildRequires:    R-CRAN-jsonlite 
Requires:         R-CRAN-solrium >= 1.0.0
Requires:         R-CRAN-crul >= 0.7.4
Requires:         R-CRAN-oai >= 0.2.2
Requires:         R-CRAN-jsonlite 

%description
Client for the web service methods provided by 'DataCite'
(<https://www.datacite.org/>), including functions to interface with their
'OAI-PMH' 'metadata' service, and a 'RESTful' search API. The API is
backed by 'SOLR', allowing expressive queries, including faceting,
statistics on variables, and 'more-like-this' queries.

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
%doc %{rlibdir}/%{packname}/ignore
%{rlibdir}/%{packname}/INDEX
