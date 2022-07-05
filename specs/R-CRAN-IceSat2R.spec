%global __brp_check_rpaths %{nil}
%global packname  IceSat2R
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          ICESat-2 Altimeter Data using R

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-lwgeom 
BuildRequires:    R-CRAN-units 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-leaflet 
BuildRequires:    R-CRAN-leafgl 
BuildRequires:    R-CRAN-leaflet.extras 
BuildRequires:    R-CRAN-leafsync 
BuildRequires:    R-CRAN-miniUI 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-rnaturalearth 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-rvest 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-lwgeom 
Requires:         R-CRAN-units 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-httr 
Requires:         R-utils 
Requires:         R-CRAN-foreach 
Requires:         R-tools 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-leaflet 
Requires:         R-CRAN-leafgl 
Requires:         R-CRAN-leaflet.extras 
Requires:         R-CRAN-leafsync 
Requires:         R-CRAN-miniUI 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-rnaturalearth 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-rvest 

%description
Programmatic connection to the 'OpenAltimetry API'
<https://openaltimetry.org/data/swagger-ui/> to download and process
'ATL03' (Global Geolocated Photon Data), 'ATL06' (Land Ice Height),
'ATL07' (Sea Ice Height), 'ATL08' (Land and Vegetation Height), 'ATL10'
(Sea Ice Freeboard), 'ATL12' (Ocean Surface Height) and 'ATL13' (Inland
Water Surface Height) 'ICESat-2' Altimeter Data. The user has the option
to download the data by selecting a bounding box from a 1- or 5-degree
grid globally utilizing a shiny application. The 'ICESat-2' mission
collects altimetry data of the Earth's surface. The sole instrument on
'ICESat-2' is the Advanced Topographic Laser Altimeter System (ATLAS)
instrument that measures ice sheet elevation change and sea ice thickness,
while also generating an estimate of global vegetation biomass. 'ICESat-2'
continues the important observations of ice-sheet elevation change,
sea-ice freeboard, and vegetation canopy height begun by 'ICESat' in 2003.

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
