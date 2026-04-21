%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ggmlR
%global packver   0.7.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.5
Release:          1%{?dist}%{?buildtag}
Summary:          'GGML' Tensor Operations for Machine Learning

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    glslc
BuildRequires:    vulkan-loader-devel
BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-generics 
Requires:         R-CRAN-generics 

%description
Provides 'R' bindings to the 'GGML' tensor library for machine learning,
optimized for 'Vulkan' GPU acceleration with a transparent CPU fallback.
The package features a 'Keras'-like sequential API and a 'PyTorch'-style
'autograd' engine for building, training, and deploying neural networks.
Key capabilities include high-performance 5D tensor operations, 'f16'
precision, and efficient quantization. It supports native 'ONNX' model
import (50+ operators) and 'GGUF' weight loading from the 'llama.cpp' and
'Hugging Face' ecosystems. Designed for zero-overhead inference via
dedicated weight buffering, it integrates seamlessly as a 'parsnip' engine
for 'tidymodels' and provides first-class learners for the 'mlr3'
framework. See <https://github.com/ggml-org/ggml> for more information
about the underlying library.

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
