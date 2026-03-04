%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  unicefData
%global packver   2.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Download Indicators from UNICEF Data Warehouse

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-memoise 
BuildRequires:    R-CRAN-countrycode 
BuildRequires:    R-CRAN-yaml 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-memoise 
Requires:         R-CRAN-countrycode 
Requires:         R-CRAN-yaml 
Requires:         R-tools 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-tidyr 

%description
An R client to fetch SDMX (Statistical Data and Metadata eXchange) CSV
series from the UNICEF Data Warehouse <https://data.unicef.org/>. Part of
a trilingual suite also available for 'Python' and 'Stata'. Features
include automatic pagination, caching with memoisation, country name
lookups, metadata versioning (vintages), and comprehensive indicator
support for SDG (Sustainable Development Goals) monitoring.

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
