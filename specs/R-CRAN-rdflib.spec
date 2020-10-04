%global packname  rdflib
%global packver   0.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.3
Release:          3%{?dist}%{?buildtag}
Summary:          Tools to Manipulate and Query Semantic Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-redland 
BuildRequires:    R-CRAN-jsonld 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-redland 
Requires:         R-CRAN-jsonld 
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 

%description
The Resource Description Framework, or 'RDF' is a widely used data
representation model that forms the cornerstone of the Semantic Web. 'RDF'
represents data as a graph rather than the familiar data table or
rectangle of relational databases. The 'rdflib' package provides a
friendly and concise user interface for performing common tasks on 'RDF'
data, such as reading, writing and converting between the various
serializations of 'RDF' data, including 'rdfxml', 'turtle', 'nquads',
'ntriples', and 'json-ld'; creating new 'RDF' graphs, and performing graph
queries using 'SPARQL'. This package wraps the low level 'redland' R
package which provides direct bindings to the 'redland' C library.
Additionally, the package supports the newer and more developer friendly
'JSON-LD' format through the 'jsonld' package. The package interface takes
inspiration from the Python 'rdflib' library.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/docker
%doc %{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
