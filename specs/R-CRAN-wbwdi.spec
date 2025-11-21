%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  wbwdi
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Seamless Access to World Bank World Development Indicators (WDI)

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-httr2 >= 1.0.0
BuildRequires:    R-CRAN-jsonlite >= 1.0.0
BuildRequires:    R-CRAN-purrr >= 1.0.0
BuildRequires:    R-CRAN-tidyr >= 1.0.0
BuildRequires:    R-CRAN-rlang >= 1.0.0
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-httr2 >= 1.0.0
Requires:         R-CRAN-jsonlite >= 1.0.0
Requires:         R-CRAN-purrr >= 1.0.0
Requires:         R-CRAN-tidyr >= 1.0.0
Requires:         R-CRAN-rlang >= 1.0.0
Requires:         R-CRAN-cli 
Requires:         R-CRAN-tibble 

%description
Access and analyze the World Bank's World Development Indicators (WDI)
using the corresponding API
<https://datahelpdesk.worldbank.org/knowledgebase/articles/889392-about-the-indicators-api-documentation>.
WDI provides more than 24,000 country or region-level indicators for
various contexts. 'wbwdi' enables users to download, process and work with
WDI series across multiple countries, aggregates, and time periods.

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
