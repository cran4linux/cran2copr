%global packname  rtsdata
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}
Summary:          R Time Series Intelligent Data Storage

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-CRAN-quantmod 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-alfred 
BuildRequires:    R-CRAN-Quandl 
BuildRequires:    R-CRAN-anytime 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-mongolite 
BuildRequires:    R-CRAN-curl 
Requires:         R-CRAN-xts 
Requires:         R-CRAN-quantmod 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-alfred 
Requires:         R-CRAN-Quandl 
Requires:         R-CRAN-anytime 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-mongolite 
Requires:         R-CRAN-curl 

%description
A tool that allows to download and save historical time series data for
future use offline. The intelligent updating functionality will only
download the new available information; thus, saving you time and Internet
bandwidth. It will only re-download the full data-set if any
inconsistencies are detected. This package supports following data
provides: 'Yahoo' (<https://finance.yahoo.com>), 'FRED'
(<https://fred.stlouisfed.org>), 'Quandl' (<https://www.quandl.com>),
'AlphaVantage' (<https://www.alphavantage.co>), 'Tiingo'
(<https://www.tiingo.com>).

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
%{rlibdir}/%{packname}/INDEX
