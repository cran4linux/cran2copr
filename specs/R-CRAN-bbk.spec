%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bbk
%global packver   0.8.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.0
Release:          1%{?dist}%{?buildtag}
Summary:          Client for Central Bank APIs

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table >= 1.17.0
BuildRequires:    R-CRAN-httr2 >= 1.0.0
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-xml2 
Requires:         R-CRAN-data.table >= 1.17.0
Requires:         R-CRAN-httr2 >= 1.0.0
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-jsonlite 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-xml2 

%description
A client for retrieving data and metadata from major central bank APIs. It
supports access to the 'Bundesbank SDMX Web Service API'
(<https://www.bundesbank.de/en/statistics/time-series-databases/help-for-sdmx-web-service/web-service-interface-data>),
the 'Swiss National Bank Data Portal' (<https://data.snb.ch/en>), the
'European Central Bank Data Portal API'
(<https://data.ecb.europa.eu/help/api/overview>), the 'Bank of England
Interactive Statistical Database'
(<https://www.bankofengland.co.uk/boeapps/database>), the 'Banco de España
API'
(<https://www.bde.es/webbe/en/estadisticas/recursos/api-estadisticas-bde.html>),
the 'Banque de France Web Service'
(<https://webstat.banque-france.fr/en/pages/guide-migration-api/>), and
'Bank of Canada Valet API' (<https://www.bankofcanada.ca/valet/docs>).

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
