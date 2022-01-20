%global __brp_check_rpaths %{nil}
%global packname  quadtree
%global packver   0.1.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.8
Release:          1%{?dist}%{?buildtag}
Summary:          Region Quadtrees for Spatial Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-Rcpp >= 1.0.5
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-stats 
Requires:         R-CRAN-Rcpp >= 1.0.5
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-methods 
Requires:         R-CRAN-raster 
Requires:         R-stats 

%description
Provides functionality for working with raster-like quadtrees (also called
“region quadtrees”), which allow for variable-sized cells. The package
allows for flexibility in the quadtree creation process.  Several
functions defining how to split and aggregate cells are provided, and
custom functions can be written for both of these processes. In addition,
quadtrees can be created using other quadtrees as “templates”, so that the
new quadtree's structure is identical to the template quadtree. The
package also includes functionality for modifying quadtrees, querying
values, saving quadtrees to a file, and calculating least-cost paths using
the quadtree as a resistance surface.

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
