%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pkmapr
%global packver   1.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Pakistan Spatial Data Toolkit

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-spdep 
BuildRequires:    R-CRAN-leaflet 
BuildRequires:    R-CRAN-jsonlite 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-spdep 
Requires:         R-CRAN-leaflet 
Requires:         R-CRAN-jsonlite 

%description
Provides a tidy interface to Pakistan's official administrative boundary
data from the United Nations Office for the Coordination of Humanitarian
Affairs (OCHA). Spatial data at country, province, district, and tehsil
levels are embedded in the package as 'sf' objects compatible with the
'tidyverse' and geospatial ecosystem. Includes utilities for geographic
dictionary lookup, coordinate reference system selection, spatial
measurement, and neighbour structure construction for use with 'spdep',
'ggplot2', 'leaflet', and related packages.

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
