%global __brp_check_rpaths %{nil}
%global packname  rgdal
%global packver   1.5-31
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.31
Release:          1%{?dist}%{?buildtag}
Summary:          Bindings for the 'Geospatial' Data Abstraction Library

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    gdal-devel >= 1.11.4
BuildRequires:    proj-devel >= 4.8.0
BuildRequires:    sqlite-devel
BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-sp >= 1.1.0
BuildRequires:    R-methods 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-sp >= 1.1.0
Requires:         R-methods 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 

%description
Provides bindings to the 'Geospatial' Data Abstraction Library ('GDAL')
(>= 1.11.4) and access to projection/transformation operations from the
'PROJ' library. Please note that 'rgdal' will be retired by the end of
2023, plan transition to sf/stars/'terra' functions using 'GDAL' and
'PROJ' at your earliest convenience. Use is made of classes defined in the
'sp' package. Raster and vector map data can be imported into R, and
raster and vector 'sp' objects exported. The 'GDAL' and 'PROJ' libraries
are external to the package, and, when installing the package from source,
must be correctly installed first; it is important that 'GDAL' < 3 be
matched with 'PROJ' < 6. From 'rgdal' 1.5-8, installed with to 'GDAL' >=3,
'PROJ' >=6 and 'sp' >= 1.4, coordinate reference systems use 'WKT2_2019'
strings, not 'PROJ' strings. 'Windows' and 'macOS' binaries (including
'GDAL', 'PROJ' and their dependencies) are provided on 'CRAN'.

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
