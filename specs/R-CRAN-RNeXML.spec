%global packname  RNeXML
%global packver   2.4.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.4.2
Release:          1%{?dist}
Summary:          Semantically Rich I/O for the 'NeXML' Format

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-XML >= 3.95
BuildRequires:    R-CRAN-ape >= 3.1
BuildRequires:    R-methods >= 3.0.0
BuildRequires:    R-CRAN-plyr >= 1.8
BuildRequires:    R-CRAN-reshape2 >= 1.2.2
BuildRequires:    R-CRAN-stringr >= 1.0
BuildRequires:    R-CRAN-dplyr >= 0.5.0
BuildRequires:    R-CRAN-tidyr >= 0.3.1
BuildRequires:    R-CRAN-httr >= 0.3
BuildRequires:    R-CRAN-uuid >= 0.1.1
BuildRequires:    R-CRAN-lazyeval >= 0.1.0
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-xml2 
Requires:         R-CRAN-XML >= 3.95
Requires:         R-CRAN-ape >= 3.1
Requires:         R-methods >= 3.0.0
Requires:         R-CRAN-plyr >= 1.8
Requires:         R-CRAN-reshape2 >= 1.2.2
Requires:         R-CRAN-stringr >= 1.0
Requires:         R-CRAN-dplyr >= 0.5.0
Requires:         R-CRAN-tidyr >= 0.3.1
Requires:         R-CRAN-httr >= 0.3
Requires:         R-CRAN-uuid >= 0.1.1
Requires:         R-CRAN-lazyeval >= 0.1.0
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-xml2 

%description
Provides access to phyloinformatic data in 'NeXML' format.  The package
should add new functionality to R such as the possibility to manipulate
'NeXML' objects in more various and refined way and compatibility with
'ape' objects.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/examples
%doc %{rlibdir}/%{packname}/simmap.md
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
