%global __brp_check_rpaths %{nil}
%global packname  alphahull
%global packver   2.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.5
Release:          1%{?dist}%{?buildtag}
Summary:          Generalization of the Convex Hull of a Sample of Points in the Plane

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-interp 
BuildRequires:    R-CRAN-R.utils 
BuildRequires:    R-CRAN-sgeostat 
BuildRequires:    R-CRAN-spatstat.geom 
BuildRequires:    R-CRAN-spatstat.random 
BuildRequires:    R-CRAN-splancs 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-interp 
Requires:         R-CRAN-R.utils 
Requires:         R-CRAN-sgeostat 
Requires:         R-CRAN-spatstat.geom 
Requires:         R-CRAN-spatstat.random 
Requires:         R-CRAN-splancs 

%description
Computation of the alpha-shape and alpha-convex hull of a given sample of
points in the plane. The concepts of alpha-shape and alpha-convex hull
generalize the definition of the convex hull of a finite set of points.
The programming is based on the duality between the Voronoi diagram and
Delaunay triangulation. The package also includes a function that returns
the Delaunay mesh of a given sample of points and its dual Voronoi diagram
in one single object.

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
