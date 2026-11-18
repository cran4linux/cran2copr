%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SurfaceMesh
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          3D Surface Meshes Based on 'CGAL'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-RcppCGAL >= 6.2.1.1
BuildRequires:    R-CRAN-Rcpp >= 1.0.9
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-BH 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-Rcpp >= 1.0.9
Requires:         R-CRAN-rgl 

%description
Processing of 3D surface meshes based on the 'C++' library 'CGAL'
(Computational Geometry Algorithms Library, <https://www.cgal.org/>).
Reads and writes common file formats for meshes and polygon soups.
Supports mesh repair, remeshing, subdivision, Boolean operations on
bounded volumes, outlier removal, surface reconstruction, (optimal)
bounding box, bounding sphere, bounding ellipsoid, convex hull, vertex
normals, surface distance metrics (such as Hausdorff), volume-overlap
similarity measures JSC (Jaccard Similarity Coefficient) and DSC (Dice
Similarity Coefficient). Adapts code from packages 'Boov' and 'cgalMeshes'
developed by Stephane Laurent.

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
