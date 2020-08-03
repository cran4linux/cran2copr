%global packname  rayshader
%global packver   0.19.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.19.2
Release:          1%{?dist}
Summary:          Create Maps and Visualize Data in 2D and 3D

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-png 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-grDevices 
BuildRequires:    R-grid 
BuildRequires:    R-utils 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-terrainmeshr 
BuildRequires:    R-CRAN-rayimage 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-png 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-rgl 
Requires:         R-grDevices 
Requires:         R-grid 
Requires:         R-utils 
Requires:         R-methods 
Requires:         R-CRAN-terrainmeshr 
Requires:         R-CRAN-rayimage 

%description
Uses a combination of raytracing and multiple hill shading methods to
produce 2D and 3D data visualizations and maps. Includes water detection
and layering functions, programmable color palette generation, several
built-in textures for hill shading, 2D and 3D plotting options, a built-in
path tracer, 'Wavefront' OBJ file export, and the ability to save 3D
visualizations to a 3D printable format.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
