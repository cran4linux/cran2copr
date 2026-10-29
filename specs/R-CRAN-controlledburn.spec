%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  controlledburn
%global packver   0.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.2
Release:          1%{?dist}%{?buildtag}
Summary:          Sparse Geometry Rasterization with Exact Coverage Fractions

License:          Apache License (== 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-vaster 
BuildRequires:    R-CRAN-wk 
BuildRequires:    R-CRAN-ximage 
BuildRequires:    R-CRAN-cpp11 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-CRAN-vaster 
Requires:         R-CRAN-wk 
Requires:         R-CRAN-ximage 

%description
Rasterize polygon, line, and point geometry without materializing any
pixel values. For polygons it computes exact coverage fractions for
polygon-grid intersections, returning sparse tables: run-length encoded
interior cells and individually weighted boundary cells. The scanline
algorithm is O(perimeter) in both time and memory, using the scan line
fill attributed to Wylie et al. (1967) <doi:10.1145/1465611.1465619>.
Exact coverage fractions use the exactextract algorithm by Daniel Baston,
vendored from the 'exactextractr' package
<doi:10.32614/CRAN.package.exactextractr>. Derived from the 'fasterize'
package by Noam Ross.

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
