%global packname  tiler
%global packver   0.2.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.5
Release:          1%{?dist}%{?buildtag}
Summary:          Create Geographic and Non-Geographic Map Tiles

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         python3dist(gdal)
BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-png 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-png 

%description
Creates geographic map tiles from geospatial map files or non-geographic
map tiles from simple image files. This package provides a tile generator
function for creating map tile sets for use with packages such as
'leaflet'. In addition to generating map tiles based on a common raster
layer source, it also handles the non-geographic edge case, producing map
tiles from arbitrary images. These map tiles, which have a non-geographic,
simple coordinate reference system (CRS), can also be used with 'leaflet'
when applying the simple CRS option. Map tiles can be created from an
input file with any of the following extensions: tif, grd and nc for
spatial maps and png, jpg and bmp for basic images. This package requires
'Python' and the 'gdal' library for 'Python'. 'Windows' users are
recommended to install 'OSGeo4W' (<https://trac.osgeo.org/osgeo4w/>) as an
easy way to obtain the required 'gdal' support for 'Python'.

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
