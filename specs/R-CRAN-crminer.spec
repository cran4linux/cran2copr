%global packname  crminer
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}
Summary:          Fetch 'Scholary' Full Text from 'Crossref'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite >= 1.4
BuildRequires:    R-CRAN-pdftools >= 1.2
BuildRequires:    R-CRAN-xml2 >= 1.1.0
BuildRequires:    R-CRAN-hoardr >= 0.5.0
BuildRequires:    R-CRAN-crul >= 0.3.4
Requires:         R-CRAN-jsonlite >= 1.4
Requires:         R-CRAN-pdftools >= 1.2
Requires:         R-CRAN-xml2 >= 1.1.0
Requires:         R-CRAN-hoardr >= 0.5.0
Requires:         R-CRAN-crul >= 0.3.4

%description
Text mining client for 'Crossref' (<https://crossref.org>). Includes
functions for getting getting links to full text of articles, fetching
full text articles from those links or Digital Object Identifiers
('DOIs'), and text extraction from 'PDFs'.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/INDEX
