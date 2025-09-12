%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ChileDataAPI
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Access Chilean Data via APIs and Curated Datasets

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-scales 
Requires:         R-utils 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-scales 

%description
Provides functions to access data from public RESTful APIs including
'FINDIC API', 'REST Countries API', 'World Bank API', and 'Nager.Date',
retrieving real-time or historical data related to Chile such as financial
indicators, holidays, international demographic and geopolitical
indicators, and more. Additionally, the package includes curated datasets
related to Chile, covering topics such as human rights violations during
the Pinochet regime, electoral data, census samples, health surveys,
seismic events, territorial codes, and environmental measurements. The
package supports research and analysis focused on Chile by integrating
open APIs with high-quality datasets from multiple domains. For more
information on the APIs, see: 'FINDIC' <https://findic.cl/>, 'REST
Countries' <https://restcountries.com/>, 'World Bank API'
<https://datahelpdesk.worldbank.org/knowledgebase/articles/889392>, and
'Nager.Date' <https://date.nager.at/Api>.

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
