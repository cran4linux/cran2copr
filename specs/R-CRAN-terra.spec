%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  terra
%global packver   1.8-29
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.8.29
Release:          1%{?dist}%{?buildtag}
Summary:          Spatial Data Analysis

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    gdal-devel
BuildRequires:    geos-devel
BuildRequires:    proj-devel
BuildRequires:    sqlite-devel
BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.10
BuildRequires:    R-methods 
Requires:         R-CRAN-Rcpp >= 1.0.10
Requires:         R-methods 

%description
Methods for spatial data analysis with vector (points, lines, polygons)
and raster (grid) data. Methods for vector data include geometric
operations such as intersect and buffer. Raster methods include local,
focal, global, zonal and geometric operations. The predict and interpolate
methods facilitate the use of regression type (interpolation, machine
learning) models for spatial prediction, including with satellite remote
sensing data. Processing of very large files is supported. See the manual
and tutorials on <https://rspatial.org/> to get started. 'terra' replaces
the 'raster' package ('terra' can do more, and it is faster and easier to
use).

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
