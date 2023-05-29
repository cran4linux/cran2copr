%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gdalraster
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bindings to the 'Geospatial Data Abstraction Library' Raster API

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.7
BuildRequires:    R-methods 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-Rcpp >= 1.0.7
Requires:         R-methods 
Requires:         R-tools 
Requires:         R-utils 

%description
Interface to the raster API of the 'Geospatial Data Abstraction Library'
('GDAL') supporting manual creation of uninitialized datasets, creation
from existing raster as template, low level I/O, configuration of virtual
raster (VRT), coordinate transformation, and access to 'gdalwarp' for
reprojection. Convenience functions facilitate working with spatial
reference systems. Calling signatures resemble the native C, C++ and
Python APIs provided by the 'GDAL' project (<https://gdal.org>). Bindings
to 'GDAL' are implemented in class 'GDALRaster' along with several
stand-alone functions. Additional functionality includes: class
'RunningStats' for efficient summary statistics on large data streams;
class 'CmbTable' for counting unique combinations of integer values with a
hash table; a raster overlay utility to identify and count unique
combinations across multiple inputs; and a calculation utility for
evaluating an R expression on raster layers with pixel coordinates
available as variables. 'gdalraster' may be suitable for applications that
primarily need low-level raster I/O, explicit manipulation of VRT format,
or prefer native 'GDAL'-like calling. Additional functionality is somewhat
aimed at thematic data analysis but may have other utility.

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
