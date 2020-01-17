%global packname  officer
%global packver   0.3.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.6
Release:          1%{?dist}
Summary:          Manipulation of Microsoft Word and PowerPoint Documents

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-zip >= 2.0.3
BuildRequires:    R-CRAN-xml2 >= 1.1.0
BuildRequires:    R-CRAN-rlang >= 0.4.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.12
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-uuid 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-htmltools 
Requires:         R-CRAN-zip >= 2.0.3
Requires:         R-CRAN-xml2 >= 1.1.0
Requires:         R-CRAN-rlang >= 0.4.0
Requires:         R-CRAN-Rcpp >= 0.12.12
Requires:         R-CRAN-R6 
Requires:         R-grDevices 
Requires:         R-CRAN-base64enc 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-uuid 
Requires:         R-stats 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-htmltools 

%description
Access and manipulate 'Microsoft Word' and 'Microsoft PowerPoint'
documents from R. The package focuses on tabular and graphical reporting
from R; it also provides two functions that let users get document content
into data objects. A set of functions lets add and remove images, tables
and paragraphs of text in new or existing documents. When working with
'PowerPoint' presentations, slides can be added or removed; shapes inside
slides can also be added or removed. When working with 'Word' documents, a
cursor can be used to help insert or delete content at a specific location
in the document. The package does not require any installation of
Microsoft products to be able to write Microsoft files.

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/doc_examples
%doc %{rlibdir}/%{packname}/template
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
