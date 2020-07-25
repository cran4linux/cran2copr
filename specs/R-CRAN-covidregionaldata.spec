%global packname  covidregionaldata
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          1%{?dist}
Summary:          Subnational Data for the Covid-19 Outbreak

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-memoise 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-yaml 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-rvest 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-countrycode 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-memoise 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-yaml 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-rvest 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-countrycode 

%description
An interface to subnational and national level Covid-19 data. For all
countries supported, this includes a daily time-series of cases. Wherever
available we also provide data on deaths, hospitalisations, and tests.
National level data is also supported using a range of data sources as
well as linelist data and links to intervention data sets. Data sources
included: WHO
<https://dashboards-dev.sprinklr.com/data/9043/global-covid19-who-gis.json>,
<https://covid19.who.in>; ACAPS interventions
<https://data.humdata.org/dataset/acaps-covid19-government-measures-dataset>;
patient linelist: <https://github.com/beoutbreakprepared/nCoV2019>),
regional data (Afghanistan:
<https://data.humdata.org/dataset/afghanistan-covid-19-statistics-per-province>;
Belgium: <https://epistat.wiv-isp.be/covid>; Brazil:
<https://github.com/wcota/covid19br>; Canada:
<https://health-infobase.canada.ca/>; Colombia:
<https://github.com/danielcs88/colombia_covid-19>; Germany:
<https://npgeo-corona-npgeo-de.hub.arcgis.com/datasets/dd4580c810204019a7b8eb3e0b329dd6_0>;
India: <https://api.covid19india.org/>; Italy:
<https://github.com/pcm-dpc/COVID-19>; Russia:
<https://github.com/grwlf/COVID-19_plus_Russia>; UK:
<https://coronavirus.data.gov.uk>,
<https://github.com/tomwhite/covid-19-uk-data>; USA:
<https://github.com/nytimes/covid-19-data>), and geocoding data (Colombia:
<https://en.wikipedia.org/wiki/ISO_3166-2:CO>; Russia:
<https://en.wikipedia.org/wiki/ISO_3166-2:RU>).

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
