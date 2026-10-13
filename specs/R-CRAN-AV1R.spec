%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  AV1R
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          1%{?dist}%{?buildtag}
Summary:          'AV1' Video Encoding for Biological Microscopy Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    ffmpeg-free-devel
BuildRequires:    vulkan-loader-devel
BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0

%description
Converts microscopy video and image data (H.264/H.265, AVI/MJPEG, TIFF
stacks) to the 'AV1' codec for compact storage, and archives 16-bit image
stacks and videos losslessly in the 'FFV1' format. Encoding runs on the
GPU via 'Vulkan' or 'VAAPI' when available and falls back to the CPU
through 'FFmpeg' and 'SVT-AV1'. Whole experiment folders can be converted
at once.

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
