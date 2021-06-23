%global __brp_check_rpaths %{nil}
%global packname  rayrender
%global packver   0.21.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.21.2
Release:          1%{?dist}%{?buildtag}
Summary:          Build and Raytrace 3D Scenes

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 1.0.0
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-png 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-decido 
BuildRequires:    R-CRAN-rayimage 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-RcppThread 
BuildRequires:    R-CRAN-spacefillr 
Requires:         R-CRAN-Rcpp >= 1.0.0
Requires:         R-parallel 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-png 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-decido 
Requires:         R-CRAN-rayimage 
Requires:         R-stats 
Requires:         R-CRAN-progress 

%description
Render scenes using pathtracing. Build 3D scenes out of spheres, cubes,
planes, disks, triangles, cones, curves, line segments, cylinders,
ellipsoids, and 3D models in the 'Wavefront' OBJ file format or the PLY
Polygon File Format. Supports several material types, textures, multicore
rendering, and tone-mapping. Based on the "Ray Tracing in One Weekend"
book series. Peter Shirley (2018) <https://raytracing.github.io>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
