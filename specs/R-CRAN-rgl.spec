%global packname  rgl
%global packver   0.104.16
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.104.16
Release:          1%{?dist}%{?buildtag}
Summary:          3D Visualization Using OpenGL

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    mesa-libGL-devel
BuildRequires:    mesa-libGLU-devel
BuildRequires:    zlib-devel
BuildRequires:    libpng-devel >= 1.2.9
BuildRequires:    freetype-devel
BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-CRAN-jsonlite >= 0.9.20
BuildRequires:    R-CRAN-manipulateWidget >= 0.9.0
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-crosstalk 
Requires:         R-CRAN-jsonlite >= 0.9.20
Requires:         R-CRAN-manipulateWidget >= 0.9.0
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-crosstalk 

%description
Provides medium to high level functions for 3D interactive graphics,
including functions modelled on base graphics (plot3d(), etc.) as well as
functions for constructing representations of geometric objects (cube3d(),
etc.).  Output may be on screen using OpenGL, or to various standard 3D
file formats including WebGL, PLY, OBJ, STL as well as 2D image formats,
including PNG, Postscript, SVG, PGF.

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
