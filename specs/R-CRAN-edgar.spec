%global packname  edgar
%global packver   2.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.2
Release:          1%{?dist}
Summary:          Platform for EDGAR Filing Management and Textual Analysis

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildArch:        noarch
BuildRequires:    R-CRAN-R.utils 
BuildRequires:    R-CRAN-tm 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-qdapRegex 
Requires:         R-CRAN-R.utils 
Requires:         R-CRAN-tm 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-qdapRegex 

%description
In the USA, companies file different forms with the U.S. Securities and
Exchange Commission (SEC) through EDGAR (Electronic Data Gathering,
Analysis, and Retrieval system). The EDGAR database automated system
collects all the different necessary filings and makes it publicly
available. Investors, regulators, and researchers often require these
forms for various purposes. This package helps in bulk data gathering and
textual analysis of EDGAR filings. It downloads filings from SEC server in
bulk with a single query. Additionally, it provides various useful
functions: extracts 8-K triggering events, extract "Business (Item 1)" and
"Management's Discussion and Analysis(Item 7)" sections of annual
statements, search filings for desired words, provides sentiment measures,
parse filing header information, and provides HTML view of SEC filings.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
