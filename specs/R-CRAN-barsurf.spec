%global __brp_check_rpaths %{nil}
%global packname  barsurf
%global packver   0.7.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.0
Release:          1%{?dist}%{?buildtag}
Summary:          Contour Plots, 3D Plots, Vector Fields and Heatmaps

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-kubik 
BuildRequires:    R-CRAN-colorspace 
Requires:         R-methods 
Requires:         R-CRAN-kubik 
Requires:         R-CRAN-colorspace 

%description
Combined contour/heatmap plots, 3d bar/surface plots, 2d/3d triangular
plots, isosurface plots and 2d/3d vector fields. By default, uses vector
graphics, but it's possible to use raster graphics for regular heatmaps.
Builds on the colorspace package (Zeileis, et al., 2020
<doi:10.18637/jss.v096.i01>), by supporting smooth multiband color
interpolation, in sRGB, HSV and HCL color spaces.

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
