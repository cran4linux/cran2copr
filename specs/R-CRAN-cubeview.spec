%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cubeview
%global packver   0.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.1
Release:          1%{?dist}%{?buildtag}
Summary:          View 3D Raster Cubes Interactively

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-stars 
BuildRequires:    R-CRAN-svglite 
BuildRequires:    R-CRAN-viridisLite 
Requires:         R-CRAN-base64enc 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-stars 
Requires:         R-CRAN-svglite 
Requires:         R-CRAN-viridisLite 

%description
Creates a 3D data cube view of a RasterStack/Brick, typically a
collection/array of RasterLayers (along z-axis) with the same geographical
extent (x and y dimensions) and resolution, provided by package 'raster'.
Slices through each dimension (x/y/z), freely adjustable in location, are
mapped to the visible sides of the cube. The cube can be freely rotated.
Zooming and panning can be used to focus on different areas of the cube.

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
