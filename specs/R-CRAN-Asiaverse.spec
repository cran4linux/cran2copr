%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Asiaverse
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          A Metapackage for Asian Countries RESTful APIs and Curated Datasets

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ChinAPIs 
BuildRequires:    R-CRAN-JapanAPIs 
BuildRequires:    R-CRAN-SouthKoreAPIs 
BuildRequires:    R-CRAN-IndiAPIs 
BuildRequires:    R-CRAN-IndonesiAPIs 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-utils 
Requires:         R-CRAN-ChinAPIs 
Requires:         R-CRAN-JapanAPIs 
Requires:         R-CRAN-SouthKoreAPIs 
Requires:         R-CRAN-IndiAPIs 
Requires:         R-CRAN-IndonesiAPIs 
Requires:         R-CRAN-cli 
Requires:         R-utils 

%description
A metapackage that brings together a comprehensive collection of R
packages providing access to APIs functions and curated datasets from
China, Japan, South Korea, India, and Indonesia. It includes real-time and
historical data through public RESTful APIs (Nager.Date, World Bank API,
REST Countries API) and extensive curated collections of open datasets
covering economics, demographics, public health, environmental data,
natural disasters, political indicators, and social metrics. Designed to
provide researchers, analysts, educators, and data scientists with
centralized access to Asian data sources, this metapackage facilitates
reproducible research, comparative analysis, and teaching applications
focused on these five major Asian countries. Included packages: -
'ChinAPIs': APIs functions and curated datasets for China and Hong Kong
covering air quality, demographics, input-output tables, epidemiology,
political structure, and social indicators. - 'JapanAPIs': APIs functions
and curated datasets for Japan including natural disasters, economic
production, vehicle industry, air quality, demographics, and
administrative divisions. - 'SouthKoreAPIs': APIs functions and curated
datasets for South Korea covering public health outbreaks, social surveys,
elections, economic indicators, natural disasters, climate data, energy
consumption, cultural information, and financial markets. - 'IndiAPIs':
APIs functions and curated datasets for India with comprehensive
collections and real-time access to economic, demographic, and
geopolitical indicators. - 'IndonesiAPIs': APIs functions and curated
datasets for Indonesia covering holidays, economic indicators, consumer
prices, poverty probability, food prices by region, tourism destinations,
and minimum wage statistics. For more information on the APIs, see:
'Nager.Date' <https://date.nager.at/Api>, 'World Bank API'
<https://datahelpdesk.worldbank.org/knowledgebase/articles/889392>, and
'REST Countries API' <https://restcountries.com/>.

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
