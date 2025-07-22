%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  geeLite
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Building and Managing Local Databases from 'Google Earth Engine'

License:          MPL-2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-rnaturalearthdata 
BuildRequires:    R-CRAN-rnaturalearth 
BuildRequires:    R-CRAN-googledrive 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-reticulate 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-geojsonio 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-tidyrgee 
BuildRequires:    R-CRAN-RSQLite 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-h3jsr 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-rgee 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-sf 
Requires:         R-CRAN-rnaturalearthdata 
Requires:         R-CRAN-rnaturalearth 
Requires:         R-CRAN-googledrive 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-reticulate 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-geojsonio 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-tidyrgee 
Requires:         R-CRAN-RSQLite 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-h3jsr 
Requires:         R-CRAN-knitr 
Requires:         R-utils 
Requires:         R-CRAN-purrr 
Requires:         R-stats 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-rgee 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-sf 

%description
Simplifies the creation, management, and updating of local databases using
data extracted from 'Google Earth Engine' ('GEE'). It integrates with
'GEE' to store, aggregate, and process spatio-temporal data, leveraging
'SQLite' for efficient, serverless storage. The 'geeLite' package provides
utilities for data transformation and supports real-time monitoring and
analysis of geospatial features, making it suitable for researchers and
practitioners in geospatial science. For details, see Kurbucz and Andrée
(2025) "Building and Managing Local Databases from Google Earth Engine
with the geeLite R Package" <https://hdl.handle.net/10986/43165>.

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
