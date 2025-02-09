%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  geometry
%global packver   0.5.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.2
Release:          1%{?dist}%{?buildtag}
Summary:          Mesh Generation and Surface Tessellation

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-magic 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-lpSolve 
BuildRequires:    R-CRAN-linprog 
BuildRequires:    R-CRAN-RcppProgress 
Requires:         R-CRAN-magic 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-lpSolve 
Requires:         R-CRAN-linprog 

%description
Makes the 'Qhull' library <http://www.qhull.org> available in R, in a
similar manner as in Octave and MATLAB. Qhull computes convex hulls,
Delaunay triangulations, halfspace intersections about a point, Voronoi
diagrams, furthest-site Delaunay triangulations, and furthest-site Voronoi
diagrams. It runs in 2D, 3D, 4D, and higher dimensions. It implements the
Quickhull algorithm for computing the convex hull. Qhull does not support
constrained Delaunay triangulations, or mesh generation of non-convex
objects, but the package does include some R functions that allow for
this.

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
