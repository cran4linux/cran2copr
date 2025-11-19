%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fasterRaster
%global packver   8.4.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          8.4.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Faster Raster and Spatial Vector Processing Using 'GRASS'

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-terra >= 1.7
BuildRequires:    R-CRAN-omnibus >= 1.2.15
BuildRequires:    R-CRAN-data.table >= 1.14.8
BuildRequires:    R-CRAN-rgrass >= 0.3.9
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-utils 
Requires:         R-CRAN-terra >= 1.7
Requires:         R-CRAN-omnibus >= 1.2.15
Requires:         R-CRAN-data.table >= 1.14.8
Requires:         R-CRAN-rgrass >= 0.3.9
Requires:         R-CRAN-DT 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-methods 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-shiny 
Requires:         R-utils 

%description
Processing of large-in-memory/large-on disk rasters and spatial vectors
using 'GRASS' <https://grass.osgeo.org/>. Most functions in the 'terra'
package are recreated. Processing of medium-sized and smaller spatial
objects will nearly always be faster using 'terra' or 'sf', but for
large-in-memory/large-on-disk objects, 'fasterRaster' may be faster. To
use most of the functions, you must have the stand-alone version (not the
'OSGeoW4' installer version) of 'GRASS' 8.0 or higher.

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
