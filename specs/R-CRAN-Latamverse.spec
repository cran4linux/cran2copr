%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Latamverse
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Latin American Data via 'RESTful' APIs and Curated Datasets

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ArgentinAPI 
BuildRequires:    R-CRAN-BrazilDataAPI 
BuildRequires:    R-CRAN-ChileDataAPI 
BuildRequires:    R-CRAN-ColombiAPI 
BuildRequires:    R-CRAN-PeruAPIs 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-utils 
Requires:         R-CRAN-ArgentinAPI 
Requires:         R-CRAN-BrazilDataAPI 
Requires:         R-CRAN-ChileDataAPI 
Requires:         R-CRAN-ColombiAPI 
Requires:         R-CRAN-PeruAPIs 
Requires:         R-CRAN-cli 
Requires:         R-utils 

%description
Brings together a comprehensive collection of R packages providing access
to API functions and curated datasets from Argentina, Brazil, Chile,
Colombia, and Peru. Includes real-time and historical data through public
'RESTful' APIs ('Nager.Date', World Bank API, REST Countries API, and
country-specific APIs) and extensive curated collections of open datasets
covering economics, demographics, public health, environmental data,
political indicators, social metrics, and cultural information. Designed
to provide researchers, analysts, educators, and data scientists with
centralized access to Latin American data sources, facilitating
reproducible research, comparative analysis, and teaching applications
focused on these five major Latin American countries. Included packages: -
'ArgentinAPI': API functions and curated datasets for Argentina covering
exchange rates, inflation, political figures, national holidays and more.
- 'BrazilDataAPI': API functions and curated datasets for Brazil covering
postal codes, banks, economic indicators, holidays, company registrations
and more. - 'ChileDataAPI': API functions and curated datasets for Chile
covering financial indicators ('UF', UTM, Dollar, Euro, Yen, Copper,
Bitcoin, 'IPSA' index), holidays and more. - 'ColombiAPI': API functions
and curated datasets for Colombia covering geographic locations, cultural
attractions, economic indicators, demographic data, national holidays and
more. - 'PeruAPIs': API functions and curated datasets for Peru covering
economic indicators, demographics, national holidays, administrative
divisions, electoral data, biodiversity and more. For more information on
the APIs, see: 'Nager.Date' <https://date.nager.at/Api>, World Bank API
<https://datahelpdesk.worldbank.org/knowledgebase/articles/889392>, REST
Countries API <https://restcountries.com/>, 'ArgentinaDatos' API
<https://argentinadatos.com/>, 'BrasilAPI' <https://brasilapi.com.br/>,
'FINDIC' <https://findic.cl/>, and API-Colombia
<https://api-colombia.com/>.

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
