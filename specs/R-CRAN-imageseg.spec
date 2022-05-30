%global __brp_check_rpaths %{nil}
%global packname  imageseg
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          1%{?dist}%{?buildtag}
Summary:          Deep Learning Models for Image Segmentation

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-keras 
BuildRequires:    R-CRAN-magick 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-dplyr 
Requires:         R-grDevices 
Requires:         R-CRAN-keras 
Requires:         R-CRAN-magick 
Requires:         R-CRAN-magrittr 
Requires:         R-methods 
Requires:         R-CRAN-purrr 
Requires:         R-stats 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-foreach 
Requires:         R-parallel 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-dplyr 

%description
A general-purpose workflow for image segmentation using TensorFlow models
based on the U-Net architecture by Ronneberger et al. (2015)
<arXiv:1505.04597> and the U-Net++ architecture by Zhou et al. (2018)
<arXiv:1807.10165>. We provide pre-trained models for assessing canopy
density and understory vegetation density from vegetation photos. In
addition, the package provides a workflow for easily creating model input
and model architectures for general-purpose image segmentation based on
grayscale or color images, both for binary and multi-class image
segmentation.

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
