%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  geodl
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Geospatial Semantic Segmentation with Torch and Terra

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-R6 >= 2.5.1
BuildRequires:    R-CRAN-psych >= 2.3.3
BuildRequires:    R-CRAN-readr >= 2.1.3
BuildRequires:    R-CRAN-terra >= 1.7.55
BuildRequires:    R-CRAN-dplyr >= 1.1.3
BuildRequires:    R-CRAN-rlang >= 1.1.1
BuildRequires:    R-CRAN-coro >= 1.0.3
BuildRequires:    R-CRAN-MultiscaleDTM >= 0.8.2
BuildRequires:    R-CRAN-torchvision >= 0.5.1
BuildRequires:    R-CRAN-luz >= 0.4.0
BuildRequires:    R-CRAN-torch >= 0.11.0
Requires:         R-CRAN-R6 >= 2.5.1
Requires:         R-CRAN-psych >= 2.3.3
Requires:         R-CRAN-readr >= 2.1.3
Requires:         R-CRAN-terra >= 1.7.55
Requires:         R-CRAN-dplyr >= 1.1.3
Requires:         R-CRAN-rlang >= 1.1.1
Requires:         R-CRAN-coro >= 1.0.3
Requires:         R-CRAN-MultiscaleDTM >= 0.8.2
Requires:         R-CRAN-torchvision >= 0.5.1
Requires:         R-CRAN-luz >= 0.4.0
Requires:         R-CRAN-torch >= 0.11.0

%description
Provides tools for semantic segmentation of geospatial data using
convolutional neural network-based deep learning. Utility functions allow
for creating masks, image chips, data frames listing image chips in a
directory, and DataSets for use within DataLoaders. Additional functions
are provided to serve as checks during the data preparation and training
process. A UNet architecture can be defined with 4 blocks in the encoder,
a bottleneck block, and 4 blocks in the decoder. The UNet can accept a
variable number of input channels, and the user can define the number of
feature maps produced in each encoder and decoder block and the
bottleneck. Users can also choose to (1) replace all rectified linear unit
(ReLU) activation functions with leaky ReLU or swish, (2) implement
attention gates along the skip connections, (3) implement squeeze and
excitation modules within the encoder blocks, (4) add residual connections
within all blocks, (5) replace the bottleneck with a modified atrous
spatial pyramid pooling (ASPP) module, and/or (6) implement deep
supervision using predictions generated at each stage in the decoder. A
unified focal loss framework is implemented after Yeung et al. (2022)
<doi:10.1016/j.compmedimag.2021.102026>. We have also implemented
assessment metrics using the 'luz' package including F1-score, recall, and
precision. Trained models can be used to predict to spatial data without
the need to generate chips from larger spatial extents. Functions are
available for performing accuracy assessment. The package relies on
'torch' for implementing deep learning, which does not require the
installation of a 'Python' environment. Raster geospatial data are handled
with 'terra'. Models can be trained using a Compute Unified Device
Architecture (CUDA)-enabled graphics processing unit (GPU); however,
multi-GPU training is not supported by 'torch' in 'R'.

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
