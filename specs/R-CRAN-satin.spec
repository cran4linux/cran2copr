%global packname  satin
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Visualisation and Analysis of Ocean Data Derived from Satellites

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ncdf4 
BuildRequires:    R-CRAN-maps 
BuildRequires:    R-CRAN-maptools 
BuildRequires:    R-CRAN-PBSmapping 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-splancs 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-geosphere 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-lubridate 
Requires:         R-CRAN-ncdf4 
Requires:         R-CRAN-maps 
Requires:         R-CRAN-maptools 
Requires:         R-CRAN-PBSmapping 
Requires:         R-grDevices 
Requires:         R-CRAN-splancs 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-geosphere 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-CRAN-lubridate 

%description
With 'satin' functions, visualisation, data extraction and further
analysis like producing climatologies from several images, and anomalies
of satellite derived ocean data can be easily done.  Reading functions can
import a user defined geographical extent of data stored in netCDF files.
Currently supported ocean data sources include NASA's Oceancolor web page
<https://oceancolor.gsfc.nasa.gov/>, sensors VIIRS-SNPP; MODIS-Terra;
MODIS-Aqua; and SeaWiFS.  Available variables from this source includes
chlorophyll concentration, sea surface temperature (SST), and several
others.  Data sources specific for SST that can be imported too includes
Pathfinder AVHRR <https://www.ncei.noaa.gov/products/avhrr-pathfinder-sst>
and GHRSST <https://www.ghrsst.org/>.  In addition, ocean productivity
data produced by Oregon State University
<http://sites.science.oregonstate.edu/ocean.productivity/> can also be
handled previous conversion from HDF4 to HDF5 format.  Many other ocean
variables can be processed by importing netCDF data files from two
European Union's Copernicus Marine Service databases
<https://marine.copernicus.eu/>, namely Global Ocean Physical Reanalysis
and Global Ocean Biogeochemistry Hindcast.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
