%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  brfinance
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Simplified Access to Brazilian Financial and Macroeconomic Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-httr2 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-sidrar 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-janitor 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-httr2 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-sidrar 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-janitor 

%description
It offers simplified access to Brazilian macroeconomic and financial
indicators selected from official sources, such as the 'IBGE' (Brazilian
Institute of Geography and Statistics) via the 'SIDRA' API and the
'Central Bank of Brazil' via the 'SGS' API. It allows users to quickly
retrieve and visualize data series such as the unemployment rate and the
Selic interest rate. This package was developed for data access and
visualization purposes, without generating forecasts or statistical
results. For more information, see the official APIs:
<https://sidra.ibge.gov.br/> and
<https://dadosabertos.bcb.gov.br/dataset/>.

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
