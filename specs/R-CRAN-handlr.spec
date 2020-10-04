%global packname  handlr
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          3%{?dist}%{?buildtag}
Summary:          Convert Among Citation Formats

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-crul 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-RefManageR 
BuildRequires:    R-CRAN-urltools 
BuildRequires:    R-CRAN-mime 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-crul 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-RefManageR 
Requires:         R-CRAN-urltools 
Requires:         R-CRAN-mime 

%description
Converts among many citation formats, including 'BibTeX', 'Citeproc',
'Codemeta', 'RDF XML', 'RIS', and 'Schema.org'. A low level 'R6' class is
provided, as well as stand-alone functions for each citation format for
both read and write.

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
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
