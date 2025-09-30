%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ColombiAPI
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Access Colombian Data via APIs and Curated Datasets

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-tibble 

%description
Provides a comprehensive interface to access diverse public data about
Colombia through multiple APIs and curated datasets. The package
integrates four different APIs: 'API-Colombia' for Colombian-specific data
including geography, culture, tourism, and government information; 'World
Bank API' for economic and demographic indicators; 'Nager.Date' for public
holidays; and 'REST Countries API' for general country information. The
package enables users to explore various aspects of Colombia such as
geographic locations, cultural attractions, economic indicators,
demographic data, and public holidays. Additionally, 'ColombiAPI' includes
curated datasets covering Bogota air stations, business and holiday dates,
public schools, Colombian coffee exports, cannabis licenses, Medellin
rainfall, malls in Bogota, as well as datasets on indigenous languages,
student admissions and school statistics, forest liana mortality,
municipal and regional data, connectivity and digital infrastructure,
program graduates, vehicle counts, international visitors, and GDP
projections. These datasets provide users with a rich and multifaceted
view of Colombian social, economic, environmental, and technological
information, making 'ColombiAPI' a comprehensive tool for exploring
Colombia's diverse data landscape. For more information on the APIs, see:
'API-Colombia' <https://api-colombia.com/>, 'Nager.Date'
<https://date.nager.at/Api>, 'World Bank API'
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
