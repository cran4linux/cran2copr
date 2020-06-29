%global packname  rayimage
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}
Summary:          Image Processing for Simulated Cameras

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-png 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-jpeg 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-progress 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-png 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-jpeg 
Requires:         R-grDevices 

%description
Uses convolution-based techniques to generate simulated camera bokeh,
depth of field, and other camera effects, using an image and an optional
depth map. Accepts both filename inputs and in-memory array
representations of images and matrices. Includes functions to perform 2D
convolutions, reorient and resize images/matrices, add image overlays,
generate camera vignette effects, and add titles to images.

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
