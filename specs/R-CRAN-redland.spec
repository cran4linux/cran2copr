%global packname  redland
%global packver   1.0.17-11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.17.11
Release:          1%{?dist}
Summary:          RDF Library Bindings in R

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    redland-devel >= 1.0.14
Requires:         redland
BuildRequires:    R-devel >= 3.1.1
Requires:         R-core >= 3.1.1
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-roxygen2 
Requires:         R-methods 
Requires:         R-CRAN-roxygen2 

%description
Provides methods to parse, query and serialize information stored in the
Resource Description Framework (RDF). RDF is described at
<http://www.w3.org/TR/rdf-primer>. This package supports RDF by
implementing an R interface to the Redland RDF C library, described at
<http://librdf.org/docs/api/index.html>. In brief, RDF provides a
structured graph consisting of Statements composed of Subject, Predicate,
and Object Nodes.

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
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/COPYRIGHTS
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/NOTICE
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
