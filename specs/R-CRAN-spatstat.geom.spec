%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  spatstat.geom
%global packver   3.3-6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.3.6
Release:          1%{?dist}%{?buildtag}
Summary:          Geometrical Functionality of the 'spatstat' Family

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-spatstat.utils >= 3.1.2
BuildRequires:    R-CRAN-spatstat.data >= 3.1
BuildRequires:    R-CRAN-spatstat.univar >= 3.1
BuildRequires:    R-CRAN-polyclip >= 1.10
BuildRequires:    R-CRAN-deldir >= 1.0.2
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
BuildRequires:    R-methods 
Requires:         R-CRAN-spatstat.utils >= 3.1.2
Requires:         R-CRAN-spatstat.data >= 3.1
Requires:         R-CRAN-spatstat.univar >= 3.1
Requires:         R-CRAN-polyclip >= 1.10
Requires:         R-CRAN-deldir >= 1.0.2
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-utils 
Requires:         R-methods 

%description
Defines spatial data types and supports geometrical operations on them.
Data types include point patterns, windows (domains), pixel images, line
segment patterns, tessellations and hyperframes. Capabilities include
creation and manipulation of data (using command line or graphical
interaction), plotting, geometrical operations (rotation, shift, rescale,
affine transformation), convex hull, discretisation and pixellation,
Dirichlet tessellation, Delaunay triangulation, pairwise distances,
nearest-neighbour distances, distance transform, morphological operations
(erosion, dilation, closing, opening), quadrat counting, geometrical
measurement, geometrical covariance, colour maps, calculus on spatial
domains, Gaussian blur, level sets of images, transects of images,
intersections between objects, minimum distance matching. (Excludes
spatial data on a network, which are supported by the package
'spatstat.linnet'.)

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
