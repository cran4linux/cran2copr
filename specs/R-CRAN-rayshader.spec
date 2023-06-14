%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rayshader
%global packver   0.35.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.35.7
Release:          1%{?dist}%{?buildtag}
Summary:          Create Maps and Visualize Data in 2D and 3D

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildRequires:    R-CRAN-rayimage >= 0.9.0
BuildRequires:    R-CRAN-rayvertex >= 0.7.6
BuildRequires:    R-CRAN-rayrender >= 0.29.6
BuildRequires:    R-CRAN-rgl >= 0.110.7
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-png 
BuildRequires:    R-CRAN-jpeg 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-grDevices 
BuildRequires:    R-grid 
BuildRequires:    R-utils 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-terrainmeshr 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-rayimage >= 0.9.0
Requires:         R-CRAN-rayvertex >= 0.7.6
Requires:         R-CRAN-rayrender >= 0.29.6
Requires:         R-CRAN-rgl >= 0.110.7
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-png 
Requires:         R-CRAN-jpeg 
Requires:         R-CRAN-magrittr 
Requires:         R-grDevices 
Requires:         R-grid 
Requires:         R-utils 
Requires:         R-methods 
Requires:         R-CRAN-terrainmeshr 

%description
Uses a combination of raytracing and multiple hill shading methods to
produce 2D and 3D data visualizations and maps. Includes water detection
and layering functions, programmable color palette generation, several
built-in textures for hill shading, 2D and 3D plotting options, a built-in
path tracer, 'Wavefront' OBJ file export, and the ability to save 3D
visualizations to a 3D printable format.

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
