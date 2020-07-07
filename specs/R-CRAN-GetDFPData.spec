%global packname  GetDFPData
%global packver   1.5.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.3
Release:          3%{?dist}
Summary:          Reading Annual Financial Reports from Bovespa's DFP, FRE and FCASystem

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-xlsx 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-lubridate 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-xlsx 
Requires:         R-stats 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-lubridate 

%description
Reads annual financial reports including assets, liabilities, dividends
history, stockholder composition and much more from Bovespa's DFP, FRE and
FCA systems
<http://www.bmfbovespa.com.br/en_us/products/listed-equities-and-derivatives/equities/listed-companies.htm>.
These are web based interfaces for all financial reports of companies
traded at Bovespa. The package is specially designed for large scale data
importation, keeping a tabular (long) structure for easier processing.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
