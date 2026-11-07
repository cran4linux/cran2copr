%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bigcurve
%global packver   0.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.0
Release:          1%{?dist}%{?buildtag}
Summary:          Adaptive Densification of Lines for Map Projections

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-cpp11 
Requires:         R-stats 

%description
Densify lines adaptively, as required by the curvature a map projection
imposes on them. Edges are read as great circle arcs, and vertices are
inserted along them only where the projected curve deviates from a
straight chord by more than a tolerance measured on the map, following the
adaptive resampling method of the 'd3-geo' 'JavaScript' library described
in Bostock (2016) <https://github.com/d3/d3-geo>. Projections are computed
with the 'PROJ' coordinate transformation library (<https://proj.org/>),
so any coordinate reference system it supports can be a target. Inputs can
be coordinate matrices, segment meshes or vertex pool topology from
'wkpool', and edges shared by neighbouring polygons receive identical new
vertices.

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
