%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  textures
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Quad Mesh Primitives and Texture Mapping for Grids

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-cpp11 
Requires:         R-graphics 
Requires:         R-grDevices 

%description
Generate quad mesh primitives from the compact specification of a regular
grid, its dimension and extent. Provides fast generation of mesh indexes
and vertices, an unexpanded intermediate form (the grid edge coordinates),
and a compact serializable specification for meshes that are generated on
demand. Meshes are 'mesh3d' objects as used by the 'rgl' package,
constructed without requiring any graphics engine, with support for
texture mapping (Heckbert (1986) <doi:10.1109/MCG.1986.276672>) where an
image is draped over a mesh whose density is independent of the image
resolution. A C++ header library is installed so that other packages may
generate mesh components via 'LinkingTo'.

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
