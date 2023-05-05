%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pedquant
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Public Economic Data and Quantitative Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-xefun > 0.1.3
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-TTR 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-PerformanceAnalytics 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-rvest 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-echarts4r 
Requires:         R-CRAN-xefun > 0.1.3
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-TTR 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-PerformanceAnalytics 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-rvest 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-echarts4r 

%description
Provides an interface to access public economic and financial data for
economic research and quantitative analysis. The data sources including
NBS, FRED, Sina, Eastmoney and etc. It also provides quantitative
functions for trading strategies based on the 'data.table', 'TTR',
'PerformanceAnalytics' and etc packages.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
