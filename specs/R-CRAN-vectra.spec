%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  vectra
%global packver   0.9.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.7
Release:          1%{?dist}%{?buildtag}
Summary:          Columnar Query Engine for Larger-than-RAM Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-libgeos 
BuildRequires:    R-parallel 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-libgeos 
Requires:         R-parallel 

%description
A minimal columnar query engine with lazy execution on datasets larger
than RAM. Provides 'dplyr'-like verbs (filter(), select(), mutate(),
group_by(), summarise(), joins, window functions) and common aggregations
(n(), sum(), mean(), min(), max(), sd(), first(), last()) backed by a pure
C11 pull-based execution engine and a custom on-disk format ('.vtr').
Reads and writes 'GeoTIFF' (including tiled and 'BigTIFF' layouts) and a
tiled raster format ('.vec') with overview pyramids and time cubes for
larger-than-RAM raster data. Streams vector operations (spatial
transforms, point-in-polygon and nearest-feature joins including a
two-sided grid-partitioned join, select-by-location, clip, erase,
dissolve, 'rasterization', 'polygonization', and contouring) through 'sf',
and runs raster operations (zonal statistics, focal windows, terrain
derivatives, resample or 'reproject' warp, polygon masking, map algebra,
and 'mosaicking') in native C or over the tiled '.vec' format, one batch
or tile at a time for data larger than RAM.

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
