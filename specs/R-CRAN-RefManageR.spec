%global packname  RefManageR
%global packver   1.2.12
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.12
Release:          3%{?dist}%{?buildtag}
Summary:          Straightforward 'BibTeX' and 'BibLaTeX' Bibliography Management

License:          GPL-2 | GPL-3 | BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lubridate >= 1.5.0
BuildRequires:    R-CRAN-bibtex >= 0.4.1
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-methods 
Requires:         R-CRAN-lubridate >= 1.5.0
Requires:         R-CRAN-bibtex >= 0.4.1
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-jsonlite 
Requires:         R-utils 
Requires:         R-CRAN-plyr 
Requires:         R-tools 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-stringr 
Requires:         R-methods 

%description
Provides tools for importing and working with bibliographic references. It
greatly enhances the 'bibentry' class by providing a class 'BibEntry'
which stores 'BibTeX' and 'BibLaTeX' references, supports 'UTF-8'
encoding, and can be easily searched by any field, by date ranges, and by
various formats for name lists (author by last names, translator by full
names, etc.). Entries can be updated, combined, sorted, printed in a
number of styles, and exported. 'BibTeX' and 'BibLaTeX' '.bib' files can
be read into 'R' and converted to 'BibEntry' objects. Interfaces to 'NCBI
Entrez', 'CrossRef', and 'Zotero' are provided for importing references
and references can be created from locally stored 'PDF' files using
'Poppler'. Includes functions for citing and generating a bibliography
with hyperlinks for documents prepared with 'RMarkdown' or 'RHTML'.

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
%doc %{rlibdir}/%{packname}/Bib
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/NEWS.md
%doc %{rlibdir}/%{packname}/Rhtml
%doc %{rlibdir}/%{packname}/Rmd
%{rlibdir}/%{packname}/INDEX
