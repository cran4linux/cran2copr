%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rGEDI
%global packver   0.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.0
Release:          1%{?dist}%{?buildtag}
Summary:          NASA's Global Ecosystem Dynamics Investigation (GEDI) Data Visualization and Processing

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-bit64 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-getPass 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-hdf5r 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-lazyeval 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-terra 
Requires:         R-methods 
Requires:         R-CRAN-bit64 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-getPass 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-hdf5r 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-lazyeval 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-sf 
Requires:         R-stats 
Requires:         R-CRAN-terra 

%description
Provides an end-to-end workflow for NASA Global Ecosystem Dynamics
Investigation (GEDI) Level 1B, Level 2A, Level 2B, Level 3, Level 4A, and
Level 4B data. Functions search NASA catalogues, download granules, stream
HDF5 products from Earthdata Cloud, and extract geolocations, waveforms,
elevation and relative-height metrics, canopy cover, plant area profiles,
and aboveground biomass. Methods quality-filter and spatially clip HDF5,
tabular, and raster products; calculate footprint and polygon statistics;
create gridded summaries; and visualize orbital tracks and measurements.
The package also simulates GEDI-like waveforms from airborne
laser-scanning point clouds and supports spatial sampling, predictive
modelling, ancillary-data extraction, and wall-to-wall upscaling with
optional Google Earth Engine workflows.

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
