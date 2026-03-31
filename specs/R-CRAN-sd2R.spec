%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sd2R
%global packver   0.1.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.7
Release:          1%{?dist}%{?buildtag}
Summary:          Stable Diffusion Image Generation

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.0
BuildRequires:    R-CRAN-ggmlR >= 0.5.0
Requires:         R-CRAN-Rcpp >= 1.0.0
Requires:         R-CRAN-ggmlR >= 0.5.0

%description
Provides Stable Diffusion image generation in R using the 'ggmlR' tensor
library. Supports text-to-image and image-to-image generation with
multiple model versions (SD 1.x, SD 2.x, 'SDXL', Flux). Implements the
full inference pipeline including CLIP text encoding, 'UNet' noise
removal, and 'VAE' encoding/decoding. Unified sd_generate() entry point
with automatic strategy selection (direct, tiled sampling, high-resolution
fix) based on output resolution and available 'VRAM'. High-resolution
generation (2K, 4K+) via tiled 'VAE' decoding, tiled diffusion sampling
('MultiDiffusion'), and classic two-pass refinement (text-to-image, then
upscale with image-to-image). Multi-GPU parallel generation via
sd_generate_multi_gpu(). Multi-GPU model parallelism via 'device_layout'
in sd_ctx(): distribute diffusion, text encoders, and 'VAE' across
separate 'Vulkan' devices. Built-in profiling (sd_profile_start(),
sd_profile_summary()) for per-stage timing of text encoding, sampling, and
'VAE' decode. Supports CPU and 'Vulkan' GPU. No 'Python' or external API
dependencies required. Cross-platform: Linux, macOS, Windows.

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
