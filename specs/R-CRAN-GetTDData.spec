%global packname  GetTDData
%global packver   1.4.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.2
Release:          2%{?dist}
Summary:          Get Data for Brazilian Bonds (Tesouro Direto)

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.3
Requires:         R-core >= 3.2.3
BuildArch:        noarch
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-bizdays 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-rvest 
BuildRequires:    R-CRAN-xml2 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-readxl 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-bizdays 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-rvest 
Requires:         R-CRAN-xml2 

%description
Downloads and aggregates data for Brazilian government issued bonds
directly from the website of Tesouro Direto
<http://www.tesouro.fazenda.gov.br/tesouro-direto-balanco-e-estatisticas>.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
