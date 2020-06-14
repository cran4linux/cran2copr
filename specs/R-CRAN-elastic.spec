%global packname  elastic
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          2%{?dist}
Summary:          General Purpose Interface to 'Elasticsearch'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-curl >= 2.2
BuildRequires:    R-CRAN-jsonlite >= 1.1
BuildRequires:    R-CRAN-crul >= 0.9.0
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-R6 
Requires:         R-CRAN-curl >= 2.2
Requires:         R-CRAN-jsonlite >= 1.1
Requires:         R-CRAN-crul >= 0.9.0
Requires:         R-utils 
Requires:         R-CRAN-R6 

%description
Connect to 'Elasticsearch', a 'NoSQL' database built on the 'Java' Virtual
Machine. Interacts with the 'Elasticsearch' 'HTTP' API
(<https://www.elastic.co/products/elasticsearch>), including functions for
setting connection details to 'Elasticsearch' instances, loading bulk
data, searching for documents with both 'HTTP' query variables and 'JSON'
based body requests. In addition, 'elastic' provides functions for
interacting with API's for 'indices', documents, nodes, clusters, an
interface to the cat API, and more.

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/examples
%doc %{rlibdir}/%{packname}/ignore
%doc %{rlibdir}/%{packname}/vign
%{rlibdir}/%{packname}/INDEX
