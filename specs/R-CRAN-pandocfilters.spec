%global packname  pandocfilters
%global packver   0.1-4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          3%{?dist}%{?buildtag}
Summary:          Pandoc Filters for R

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         pandoc
BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-utils 
Requires:         R-CRAN-jsonlite 
Requires:         R-utils 

%description
The document converter 'pandoc' <http://pandoc.org/> is widely used in the
R community. One feature of 'pandoc' is that it can produce and consume
JSON-formatted abstract syntax trees (AST). This allows to transform a
given source document into JSON-formatted AST, alter it by so called
filters and pass the altered JSON-formatted AST back to 'pandoc'. This
package provides functions which allow to write such filters in native R
code. Although this package is inspired by the Python package
'pandocfilters' <https://github.com/jgm/pandocfilters/>, it provides
additional convenience functions which make it simple to use the
'pandocfilters' package as a report generator. Since 'pandocfilters'
inherits most of it's functionality from 'pandoc' it can create documents
in many formats (for more information see <http://pandoc.org/>) but is
also bound to the same limitations as 'pandoc'.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/INDEX
