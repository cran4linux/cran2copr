%global packname  RJSONIO
%global packver   1.3-1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.1.4
Release:          2%{?dist}
Summary:          Serialize R Objects to JSON, JavaScript Object Notation

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-methods 
Requires:         R-methods 

%description
This is a package that allows conversion to and from data in Javascript
object notation (JSON) format. This allows R objects to be inserted into
Javascript/ECMAScript/ActionScript code and allows R programmers to read
and convert JSON content to R objects. This is an alternative to rjson
package. Originally, that was too slow for converting large R objects to
JSON and was not extensible.  rjson's performance is now similar to this
package, and perhaps slightly faster in some cases. This package uses
methods and is readily extensible by defining methods for different
classes, vectorized operations, and C code and callbacks to R functions
for deserializing JSON objects to R. The two packages intentionally share
the same basic interface. This package (RJSONIO) has many additional
options to allow customizing the generation and processing of JSON
content. This package uses libjson rather than implementing yet another
JSON parser. The aim is to support other general projects by building on
their work, providing feedback and benefit from their ongoing development.

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
%doc %{rlibdir}/%{packname}/sampleData
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
