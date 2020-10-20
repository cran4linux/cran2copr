%global packname  spex
%global packver   0.7.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.1
Release:          1%{?dist}%{?buildtag}
Summary:          Spatial Extent Tools

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.5
Requires:         R-core >= 3.2.5
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-quadmesh 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-reproj 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-crsmeta 
Requires:         R-methods 
Requires:         R-CRAN-quadmesh 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-reproj 
Requires:         R-CRAN-sp 
Requires:         R-stats 
Requires:         R-CRAN-crsmeta 

%description
Functions to produce a fully fledged 'geo-spatial' object extent as a
'SpatialPolygonsDataFrame'. Also included are functions to generate
polygons from raster data using 'quadmesh' techniques, a round number
buffered extent, and general spatial-extent and 'raster-like' extent
helpers missing from the originating packages. Some latitude-based tools
for polar maps are included.

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
