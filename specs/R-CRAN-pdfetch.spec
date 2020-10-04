%global packname  pdfetch
%global packver   0.2.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.4
Release:          3%{?dist}%{?buildtag}
Summary:          Fetch Economic and Financial Time Series Data from PublicSources

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-xml2 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-xts 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-xml2 

%description
Download economic and financial time series from public sources, including
the St Louis Fed's FRED system, Yahoo Finance, the US Bureau of Labor
Statistics, the US Energy Information Administration, the World Bank,
Eurostat, the European Central Bank, the Bank of England, the UK's Office
of National Statistics, Deutsche Bundesbank, and INSEE.

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
%doc %{rlibdir}/%{packname}/tests
%{rlibdir}/%{packname}/INDEX
