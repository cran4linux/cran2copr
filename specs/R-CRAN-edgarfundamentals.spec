%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  edgarfundamentals
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Retrieve Fundamental Financial Data from SEC 'EDGAR'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite >= 1.8.0
BuildRequires:    R-CRAN-httr >= 1.4.0
BuildRequires:    R-CRAN-dplyr >= 1.1.0
BuildRequires:    R-CRAN-tidyquant >= 1.0.0
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-jsonlite >= 1.8.0
Requires:         R-CRAN-httr >= 1.4.0
Requires:         R-CRAN-dplyr >= 1.1.0
Requires:         R-CRAN-tidyquant >= 1.0.0
Requires:         R-CRAN-rlang 

%description
Provides a simple, ticker-based interface for retrieving fundamental
financial data from the United States Securities and Exchange Commission's
'EDGAR' 'XBRL' API <https://www.sec.gov/edgar/sec-api-documentation>.
Functions return key financial ratios including earnings per share, return
on equity, return on assets, debt-to-equity, current ratio, gross margin,
operating margin, net margin, price-to-earnings, price-to-book, and
dividend yield for any publicly traded U.S. company. Data is sourced
directly from company 10-K annual filings, requiring no API key or paid
subscription. Designed for use in quantitative finance courses and
research workflows.

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
