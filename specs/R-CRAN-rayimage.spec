%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rayimage
%global packver   0.26.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.26.1
Release:          1%{?dist}%{?buildtag}
Summary:          Image Processing for Simulated Cameras

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-png 
BuildRequires:    R-CRAN-jpeg 
BuildRequires:    R-grDevices 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-tiff 
BuildRequires:    R-CRAN-systemfonts 
BuildRequires:    R-CRAN-ragg 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-tinydng 
BuildRequires:    R-CRAN-stbimageheaders 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-png 
Requires:         R-CRAN-jpeg 
Requires:         R-grDevices 
Requires:         R-grid 
Requires:         R-CRAN-tiff 
Requires:         R-CRAN-systemfonts 
Requires:         R-CRAN-ragg 

%description
Uses convolution-based techniques to generate simulated camera bokeh,
depth of field, and other camera effects, using an image and an optional
depth map. Accepts both filename inputs and in-memory array
representations of images and matrices, including common raster formats
such as 'JPEG', 'PNG', 'TIFF', 'TGA', 'BMP', 'PSD', 'GIF', 'HDR', 'PIC',
'PNM', 'DNG', and 'EXR'. Includes functions to perform 2D convolutions,
color correction, colorspace conversion, image/matrix reorientation and
resizing, image and text overlays, exposure adjustment, camera vignette
effects, and image titles.

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
