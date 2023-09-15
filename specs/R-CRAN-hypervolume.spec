%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  hypervolume
%global packver   3.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          High Dimensional Geometry, Set Operations, Projection, and Inference Using Kernel Density Estimation, Support Vector Machines, and Convex Hulls

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-maps 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-geometry 
BuildRequires:    R-CRAN-ks 
BuildRequires:    R-CRAN-hitandrun 
BuildRequires:    R-CRAN-pdist 
BuildRequires:    R-CRAN-fastcluster 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-palmerpenguins 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp 
Requires:         R-methods 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-maps 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-geometry 
Requires:         R-CRAN-ks 
Requires:         R-CRAN-hitandrun 
Requires:         R-CRAN-pdist 
Requires:         R-CRAN-fastcluster 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-terra 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doParallel 
Requires:         R-parallel 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-palmerpenguins 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-caret 

%description
Estimates the shape and volume of high-dimensional datasets and performs
set operations: intersection / overlap, union, unique components,
inclusion test, and hole detection. Uses stochastic geometry approach to
high-dimensional kernel density estimation, support vector machine
delineation, and convex hull generation. Applications include modeling
trait and niche hypervolumes and species distribution modeling.

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
