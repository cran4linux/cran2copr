%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ggmlR
%global packver   0.6.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.1
Release:          1%{?dist}%{?buildtag}
Summary:          'GGML' Tensor Operations for Machine Learning

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0

%description
Provides 'R' bindings to the 'GGML' tensor library for machine learning,
designed primarily for 'Vulkan' GPU acceleration with full CPU fallback.
'Vulkan' support is auto-detected at build time on Linux (when
'libvulkan-dev' and 'glslc' are installed) and on Windows (when 'Vulkan'
'SDK' is installed and 'VULKAN_SDK' environment variable is set); all
operations fall back to CPU transparently when no GPU is available.
Implements tensor operations, neural network layers, quantization, and a
'Keras'-like sequential model API for building and training networks.
Includes 'AdamW' (Adam with Weight decay) and 'SGD' (Stochastic Gradient
Descent) optimizers with 'MSE' (Mean Squared Error) and cross-entropy
losses. Also provides a dynamic 'autograd' engine ('PyTorch'-style) with
data-parallel training via 'dp_train()', broadcast arithmetic, 'f16'
(half-precision) support on 'Vulkan' GPU, and a multi-head attention layer
for building Transformer architectures. Serves as backend for 'LLM' (Large
Language Model) inference via 'llamaR' and Stable Diffusion image
generation via 'sdR'. See <https://github.com/ggml-org/ggml> for more
information about the underlying library.

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
