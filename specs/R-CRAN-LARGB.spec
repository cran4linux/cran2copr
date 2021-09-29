%global __brp_check_rpaths %{nil}
%global packname  LARGB
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Leaf Area Determination from Visual Image

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-imager 
BuildRequires:    R-CRAN-dplyr 
Requires:         R-CRAN-imager 
Requires:         R-CRAN-dplyr 

%description
Measurements of leaf area are important in the studies of plant biological
characteristics. High-throughput plant phenotyping using image analysis is
the key area in the domain of plant phenotyping. For determining the leaf
area, the RGB image is converted into the grayscale image by simply
averaging the Red(R), Green (G) and Blue (B) pixel values. Grayscale image
is then converted into a binary image using Otsu’s thresholding method
Otsu, N. (1979) <doi:10.1109/TSMC.1979.4310076> to separate plant area
from the background (image segmentation). The segmentation process was
accomplished by selecting the pixels with values over the threshold value
belonging to the plant region and other pixels to the background region.
The resulting binary image consists of white and black pixels representing
the plant and background regions, respectively. Finally, the number of
pixels inside the plant region was counted and converted to square
centimetres (cm2) using the reference object (any object whose actual area
is known previously) to get the projected leaf area.

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
