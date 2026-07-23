%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pdokr
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Access Open Geodata from the Dutch 'PDOK' Platform

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-httr2 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-httr2 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-tibble 

%description
Tools to discover, download, and spatially filter open geographic data
from 'PDOK' (Publieke Dienstverlening Op de Kaart), the national geodata
platform of the Netherlands. Datasets and their layers are searched and
loaded as vector simple feature ('sf') objects through 'OGC' API Features
endpoints, with automatic pagination and explicit coordinate reference
system handling. Loaded layers can be filtered by any polygon area, and
addresses or place names can be geocoded through the 'PDOK' location
server. The focus is on vector feature data; raster, tile, and coverage
services are out of scope. See <https://www.pdok.nl/> for more information
about the platform and its services.

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
