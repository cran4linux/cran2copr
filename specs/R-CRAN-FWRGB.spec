%global __brp_check_rpaths %{nil}
%global packname  FWRGB
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Fresh Weight Determination from Visual Image of the Plant

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-imager 
BuildRequires:    R-CRAN-neuralnet 
BuildRequires:    R-stats 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-imager 
Requires:         R-CRAN-neuralnet 
Requires:         R-stats 

%description
Fresh biomass determination is the key to evaluating crop genotypes'
response to diverse input and stress conditions and forms the basis for
calculating net primary production. However, as conventional phenotyping
approaches for measuring fresh biomass is time-consuming, laborious and
destructive, image-based phenotyping methods are being widely used now. In
the image-based approach, the fresh weight of the above-ground part of the
plant depends on the projected area. For determining the projected area,
the visual image of the plant is converted into the grayscale image by
simply averaging the Red(R), Green (G) and Blue (B) pixel values.
Grayscale image is then converted into a binary image using Otsu’s
thresholding method Otsu, N. (1979) <doi:10.1109/TSMC.1979.4310076> to
separate plant area from the background (image segmentation). The
segmentation process was accomplished by selecting the pixels with values
over the threshold value belonging to the plant region and other pixels to
the background region. The resulting binary image consists of white and
black pixels representing the plant and background regions. Finally, the
number of pixels inside the plant region was counted and converted to
square centimetres (cm2) using the reference object (any object whose
actual area is known previously) to get the projected area. After that,
the projected area is used as input to the machine learning model (Linear
Model, Artificial Neural Network, and Support Vector Regression) to
determine the plant's fresh weight.

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
