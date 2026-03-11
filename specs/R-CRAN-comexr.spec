%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  comexr
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Client for the Brazilian Foreign Trade Statistics API ('ComexStat')

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.6.0
BuildRequires:    R-CRAN-httr2 >= 1.0.0
Requires:         R-CRAN-cli >= 3.6.0
Requires:         R-CRAN-httr2 >= 1.0.0

%description
Interface to the 'ComexStat' API <https://comexstat.mdic.gov.br/> from the
Brazilian Ministry of Development, Industry, Trade and Services (MDIC).
Provides access to detailed export and import data, including general
trade statistics (1997-present), city-level data, historical data
(1989-1996), and auxiliary tables with product codes (NCM - Nomenclatura
Comum do Mercosul, NBM - Nomenclatura Brasileira de Mercadorias, HS -
Harmonized System), countries, economic classifications (CGCE -
Classificacao por Grandes Categorias Economicas, SITC - Standard
International Trade Classification, ISIC - International Standard
Industrial Classification), and other categories. Uses only 'httr2' for
HTTP requests and 'cli' for console messages.

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
