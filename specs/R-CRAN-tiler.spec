%global packname  tiler
%global packver   0.2.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.4
Release:          1%{?dist}
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
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/maps
%doc %{rlibdir}/%{packname}/python
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
