%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rembg
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Remove Image Backgrounds with Pre-Trained Segmentation Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-onnxr 
BuildRequires:    R-CRAN-jpeg 
BuildRequires:    R-CRAN-png 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-onnxr 
Requires:         R-CRAN-jpeg 
Requires:         R-CRAN-png 
Requires:         R-CRAN-Matrix 
Requires:         R-tools 
Requires:         R-utils 

%description
Remove the background from an image using pre-trained deep learning
segmentation models ('U-2-Net', 'ISNet', 'BiRefNet' and others) run
through the 'ONNX' Runtime via the 'onnxr' package. Given an image, a
model predicts a foreground alpha matte which is composited into a cutout
with a transparent (or solid-colour) background; optional closed-form
alpha matting (ported from 'pymatting') refines soft edges. An R port of
the Python 'rembg' package (<https://github.com/danielgatis/rembg>).
Models are downloaded on first use and cached in a per-user cache
directory.

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
