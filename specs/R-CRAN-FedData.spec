%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  FedData
%global packver   4.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Functions to Automate Downloading Geospatial Data Available from Several Federated Data Sources

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-terra >= 1.0
BuildRequires:    R-CRAN-sf >= 1.0
BuildRequires:    R-CRAN-arcgislayers >= 0.2.0
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-readr 
Requires:         R-CRAN-terra >= 1.0
Requires:         R-CRAN-sf >= 1.0
Requires:         R-CRAN-arcgislayers >= 0.2.0
Requires:         R-CRAN-curl 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-readr 

%description
Functions to automate downloading geospatial data available from several
federated data sources (mainly sources maintained by the US Federal
government). Currently, the package enables extraction from nine datasets:
The National Elevation Dataset digital elevation models (1 and 1/3
arc-second; USGS); The National Hydrography Dataset (USGS); The Soil
Survey Geographic (SSURGO) database from the National Cooperative Soil
Survey (NCSS), which is led by the Natural Resources Conservation Service
(NRCS) under the USDA; the Global Historical Climatology Network (GHCN),
coordinated by National Climatic Data Center at NOAA; the Daymet gridded
estimates of daily weather parameters for North America, version 4,
available from the Oak Ridge National Laboratory's Distributed Active
Archive Center (DAAC); the International Tree Ring Data Bank; the National
Land Cover Database (NLCD); the Cropland Data Layer from the National
Agricultural Statistics Service; and the PAD-US dataset of protected area
boundaries from the USGS.

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
