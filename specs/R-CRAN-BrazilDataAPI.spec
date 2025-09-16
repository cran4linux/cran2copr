%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BrazilDataAPI
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Access Brazilian Data via APIs and Curated Datasets

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
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-tibble 
Requires:         R-utils 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-tibble 

%description
Provides functions to access data from the 'BrasilAPI', 'REST Countries
API', 'Nager.Date API', and 'World Bank API', related to Brazil's postal
codes, banks, holidays, company registrations, international country
indicators, public holidays information, and economic development data.
Additionally, the package includes curated datasets related to Brazil,
covering topics such as demographic data (males and females by state and
year), river levels, environmental emission factors, film festivals, and
yellow fever outbreak records. The package supports research and analysis
focused on Brazil by integrating open APIs with high-quality datasets from
multiple domains. For more information on the APIs, see: 'BrasilAPI'
<https://brasilapi.com.br/>, 'Nager.Date' <https://date.nager.at/Api>,
'World Bank API'
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
