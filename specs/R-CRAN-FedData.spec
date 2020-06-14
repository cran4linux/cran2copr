%global packname  FedData
%global packver   2.5.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.5.7
Release:          2%{?dist}
Summary:          Functions to Automate Downloading Geospatial Data Available fromSeveral Federated Data Sources

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-devtools 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-rgeos 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-ncdf4 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-xml2 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-devtools 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-curl 
Requires:         R-methods 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-rgeos 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-ncdf4 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-xml2 

%description
Functions to automate downloading geospatial data available from several
federated data sources (mainly sources maintained by the US Federal
government). Currently, the package enables extraction from seven
datasets: The National Elevation Dataset digital elevation models (1 and
1/3 arc-second; USGS); The National Hydrography Dataset (USGS); The Soil
Survey Geographic (SSURGO) database from the National Cooperative Soil
Survey (NCSS), which is led by the Natural Resources Conservation Service
(NRCS) under the USDA; the Global Historical Climatology Network (GHCN),
coordinated by National Climatic Data Center at NOAA; the Daymet gridded
estimates of daily weather parameters for North America, version 3,
available from the Oak Ridge National Laboratory's Distributed Active
Archive Center (DAAC); the International Tree Ring Data Bank; and the
National Land Cover Database (NLCD).

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
