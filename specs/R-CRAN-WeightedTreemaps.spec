%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  WeightedTreemaps
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Generate and Plot Voronoi or Sunburst Treemaps from Hierarchical Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-BH 
BuildRequires:    R-CRAN-RcppCGAL 
Requires:         R-CRAN-colorspace 
Requires:         R-CRAN-dplyr 
Requires:         R-grid 
Requires:         R-CRAN-lattice 
Requires:         R-methods 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-tibble 

%description
Treemaps are a visually appealing graphical representation of numerical
data using a space-filling approach. A plane or 'map' is subdivided into
smaller areas called cells.  The cells in the map are scaled according to
an underlying metric which allows to grasp the hierarchical organization
and relative importance of many objects at once. This package contains two
different implementations of treemaps, Voronoi treemaps and Sunburst
treemaps.  The Voronoi treemap function subdivides the plot area in
polygonal cells according to the highest hierarchical level, then
continues to subdivide those parental cells on the next lower hierarchical
level, and so on. The Sunburst treemap is a computationally less demanding
treemap that does not require iterative refinement, but simply generates
circle sectors that are sized according to predefined weights.  The
Voronoi tesselation is based on functions from Paul Murrell (2012)
<https://www.stat.auckland.ac.nz/~paul/Reports/VoronoiTreemap/voronoiTreeMap.html>.

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
