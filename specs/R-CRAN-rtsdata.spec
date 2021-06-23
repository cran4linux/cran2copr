%global __brp_check_rpaths %{nil}
%global packname  rtsdata
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
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
BuildRequires:    R-CRAN-brotli 
BuildRequires:    R-CRAN-curl 
Requires:         R-CRAN-xts 
Requires:         R-CRAN-quantmod 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-alfred 
Requires:         R-CRAN-Quandl 
Requires:         R-CRAN-anytime 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-mongolite 
Requires:         R-CRAN-brotli 
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

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
