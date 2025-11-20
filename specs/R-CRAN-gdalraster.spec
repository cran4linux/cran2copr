%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gdalraster
%global packver   2.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bindings to 'GDAL'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.7
BuildRequires:    R-CRAN-bit64 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-nanoarrow 
BuildRequires:    R-stats 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-wk 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-yyjsonr 
BuildRequires:    R-CRAN-RcppInt64 
Requires:         R-CRAN-Rcpp >= 1.0.7
Requires:         R-CRAN-bit64 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-methods 
Requires:         R-CRAN-nanoarrow 
Requires:         R-stats 
Requires:         R-tools 
Requires:         R-utils 
Requires:         R-CRAN-wk 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-yyjsonr 

%description
API bindings to the Geospatial Data Abstraction Library ('GDAL',
<https://gdal.org>). Implements the 'GDAL' Raster and Vector Data Models.
Bindings are implemented with 'Rcpp' modules. Exposed C++ classes and
stand-alone functions wrap much of the 'GDAL' API and provide additional
functionality. Calling signatures resemble the native C, C++ and Python
APIs provided by the 'GDAL' project. Class 'GDALRaster' encapsulates a
'GDALDataset' and its raster band objects. Class 'GDALVector' encapsulates
an 'OGRLayer' and the 'GDALDataset' that contains it. Initial bindings are
provided to the unified 'gdal' command line interface added in 'GDAL'
3.11. C++ stand-alone functions provide bindings to most 'GDAL'
"traditional" raster and vector utilities, including 'OGR' facilities for
vector geoprocessing, several algorithms, as well as the Geometry API
('GEOS' via 'GDAL' headers), the Spatial Reference Systems API, and
methods for coordinate transformation. Bindings to the Virtual Systems
Interface ('VSI') API implement standard file system operations abstracted
for URLs, cloud storage services, 'Zip'/'GZip'/'7z'/'RAR', in-memory
files, as well as regular local file systems. This provides a single
interface for operating on file system objects that works the same for any
storage backend. A custom raster calculator evaluates a user-defined R
expression on a layer or stack of layers, with pixel x/y available as
variables in the expression. Raster 'combine()' identifies and counts
unique pixel combinations across multiple input layers, with optional
raster output of the pixel-level combination IDs. Basic plotting
capability is provided for raster and vector display. 'gdalraster' leans
toward minimalism and the use of simple, lightweight objects for holding
raw data. Currently, only minimal S3 class interfaces have been
implemented for selected R objects that contain spatial data. 'gdalraster'
may be useful in applications that need scalable, low-level I/O, or prefer
a direct 'GDAL' API.

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
