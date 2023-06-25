%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cgalMeshes
%global packver   2.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          R6 Based Utilities for 3D Meshes using 'CGAL'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    gmp-devel
BuildRequires:    mpfr-devel
BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-Rcpp >= 1.0.9
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-grDevices 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-onion 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-BH 
BuildRequires:    R-CRAN-RcppCGAL 
BuildRequires:    R-CRAN-RcppColors 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-Rcpp >= 1.0.9
Requires:         R-CRAN-data.table 
Requires:         R-grDevices 
Requires:         R-methods 
Requires:         R-CRAN-onion 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-rgl 
Requires:         R-tools 

%description
Provides some utilities for 3D meshes: clipping of a mesh to the volume
bounded by another mesh, decomposition into convex parts, distance between
a mesh and a point, Hausdorff distance between two meshes, triangulation,
geodesic distance, Boolean operations (intersection, union, difference),
Minkowski sum, subdivision algorithms, random sampling on a mesh, volume,
area, and centroid. Also provides two algorithms for surface
reconstruction from a cloud of points. Meshes are represented by R6
classes. All algorithms are performed by the 'C++' library 'CGAL'
(<https://www.cgal.org/>).

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
