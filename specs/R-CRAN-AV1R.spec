%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  AV1R
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
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
Converts legacy microscopy video formats (H.264/H.265, AVI/MJPEG, TIFF
stacks) to the modern 'AV1' codec with minimal quality loss. Typical use
cases include compressing large TIFF stacks from confocal microscopy and
time-lapse experiments from hundreds of gigabytes to manageable sizes,
re-encoding MP4 files exported from 'CellProfiler', 'ImageJ'/'Fiji', and
microscope software with approximately 2x better compression at the same
visual quality, and converting legacy AVI (MJPEG) and H.265 recordings to
a single patent-free format suited for long-term archival. Automatically
selects the best available backend: GPU hardware acceleration via 'Vulkan'
'VK_KHR_VIDEO_ENCODE_AV1' or 'VAAPI' (tested on AMD RDNA4; bundled
headers, builds with any 'Vulkan' SDK >= 1.3.275), with automatic fallback
to CPU encoding through 'FFmpeg' and 'SVT-AV1'. User controls quality via
a single CRF parameter; each backend adapts automatically (CPU and Vulkan
use CRF directly, VAAPI targets 55 percent of input bitrate). TIFF stacks
use near-lossless CRF 5 by default, with optional proportional scaling via
tiff_scale (multiplier or bounding box, aspect ratio always preserved).
Small frames are automatically scaled up to meet hardware encoder
minimums. Audio tracks are preserved automatically. Provides a simple R
API for batch conversion of entire experiment folders.

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
