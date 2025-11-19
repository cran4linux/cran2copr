%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  geocodebr
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Geolocalização De Endereços Brasileiros (Geocoding Brazilian Addresses)

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-arrow >= 15.0.1
BuildRequires:    R-CRAN-httr2 >= 1.0.0
BuildRequires:    R-CRAN-enderecobr >= 0.4.1
BuildRequires:    R-CRAN-nanoarrow >= 0.3.0.1
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-duckdb 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-h3r 
BuildRequires:    R-CRAN-parallelly 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-sfheaders 
BuildRequires:    R-tools 
Requires:         R-CRAN-arrow >= 15.0.1
Requires:         R-CRAN-httr2 >= 1.0.0
Requires:         R-CRAN-enderecobr >= 0.4.1
Requires:         R-CRAN-nanoarrow >= 0.3.0.1
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-duckdb 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-h3r 
Requires:         R-CRAN-parallelly 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-sfheaders 
Requires:         R-tools 

%description
Método simples e eficiente de geolocalizar dados no Brasil. O pacote é
baseado em conjuntos de dados espaciais abertos de endereços brasileiros,
utilizando como fonte principal o Cadastro Nacional de Endereços para Fins
Estatísticos (CNEFE). O CNEFE é publicado pelo Instituto Brasileiro de
Geografia e Estatística (IBGE), órgão oficial de estatísticas e geografia
do Brasil. (A simple and efficient method for geolocating data in Brazil.
The package is based on open spatial datasets of Brazilian addresses,
primarily using the Cadastro Nacional de Endereços para Fins Estatísticos
(CNEFE), published by the Instituto Brasileiro de Geografia e Estatística
(IBGE), Brazil's official statistics and geography agency.)

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
