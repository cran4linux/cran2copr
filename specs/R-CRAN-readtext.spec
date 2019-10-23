%global packname  readtext
%global packver   0.75
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.75
Release:          1%{?dist}
Summary:          Import and Handling for Plain and Formatted Text Files

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite >= 0.9
BuildRequires:    R-CRAN-antiword 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-pdftools 
BuildRequires:    R-CRAN-readODS 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-streamR 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-striprtf 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-utils 
Requires:         R-CRAN-jsonlite >= 0.9
Requires:         R-CRAN-antiword 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-pdftools 
Requires:         R-CRAN-readODS 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-streamR 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-striprtf 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-xml2 
Requires:         R-utils 

%description
Functions for importing and handling text files and formatted text files
with additional meta-data, such including '.csv', '.tab', '.json', '.xml',
'.html', '.pdf', '.doc', '.docx', '.rtf', '.xls', '.xlsx', and others.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%license %{rlibdir}/%{packname}/LICENSE.txt
%{rlibdir}/%{packname}/INDEX
