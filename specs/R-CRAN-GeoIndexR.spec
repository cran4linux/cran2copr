%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  GeoIndexR
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Computation of Spectral and Geospatial Indices from Multispectral Raster Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-terra >= 1.7.0
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
Requires:         R-CRAN-terra >= 1.7.0
Requires:         R-graphics 
Requires:         R-stats 

%description
A unified, fast, and extensible framework for calculating spectral and
geospatial indices from multispectral raster datasets (e.g., NDVI -
Normalized Difference Vegetation Index, NDWI - Normalized Difference Water
Index, MNDWI - Modified Normalized Difference Water Index, NDBI -
Normalized Difference Built-up Index, SAVI - Soil Adjusted Vegetation
Index, EVI - Enhanced Vegetation Index, GNDVI - Green Normalized
Difference Vegetation Index, NDMI - Normalized Difference Moisture Index,
BSI - Bare Soil Index). Designed around 'terra' 'SpatRaster' objects, it
supports multi-band rasters, automatic band resolution, sensor presets
(Sentinel-2, Landsat-8/9), customizable index parameters, vectorized
computations, and comprehensive validation. Methods based on Rouse et al.
(1973) , McFeeters (1996) <doi:10.1080/01431169608948714>, Xu (2006)
<doi:10.1080/01431160600589179>, Zha et al. (2003)
<doi:10.1016/S0034-4257(03)00087-7>, Huete (1988)
<doi:10.1016/0034-4257(88)90106-X>, Gitelson et al. (1996)
<doi:10.1016/S0034-4257(96)00072-7>, Wilson and Sader (2002)
<doi:10.1016/S0034-4257(01)00318-2>, and Rikimaru et al. (2002).

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
