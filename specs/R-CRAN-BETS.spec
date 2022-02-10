%global __brp_check_rpaths %{nil}
%global packname  BETS
%global packver   0.4.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.9
Release:          1%{?dist}%{?buildtag}
Summary:          Brazilian Economic Time Series

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildArch:        noarch
BuildRequires:    R-CRAN-rstudioapi >= 0.4
BuildRequires:    R-CRAN-shiny >= 0.13
BuildRequires:    R-CRAN-miniUI >= 0.1.1
BuildRequires:    R-CRAN-grnn 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-urca 
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-foreign 
BuildRequires:    R-CRAN-seasonal 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-dygraphs 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-webshot 
BuildRequires:    R-CRAN-RMySQL 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-rjson 
BuildRequires:    R-CRAN-rvest 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-sqldf 
Requires:         R-CRAN-rstudioapi >= 0.4
Requires:         R-CRAN-shiny >= 0.13
Requires:         R-CRAN-miniUI >= 0.1.1
Requires:         R-CRAN-grnn 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-urca 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-foreign 
Requires:         R-CRAN-seasonal 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-dygraphs 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-webshot 
Requires:         R-CRAN-RMySQL 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-rjson 
Requires:         R-CRAN-rvest 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-sqldf 

%description
It provides access to and information about the most important Brazilian
economic time series - from the Getulio Vargas Foundation
<http://portal.fgv.br/en>, the Central Bank of Brazil
<http://www.bcb.gov.br> and the Brazilian Institute of Geography and
Statistics <http://www.ibge.gov.br>. It also presents tools for managing,
analysing (e.g. generating dynamic reports with a complete analysis of a
series) and exporting these time series.

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
