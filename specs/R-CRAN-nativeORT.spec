%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  nativeORT
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Native 'R' 'ONNX' Runtime

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-glue 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-glue 

%description
Provides 'R' native 'ONNX' model inference without requiring 'Python',
'reticulate' bindings, or 'TensorFlow'. This package directly binds the
'ONNX Runtime' C API via 'Rcpp', enabling real-time inference for '.onnx'
engines, all within 'R'. Standard CPU execution is supported as well as
the 'CoreML' Execution Provider (CEP) for Apple Silicon, all without
external bindings. This package handles OS detection, linking 'ONNX'
libraries, and inference. For more information about 'ONNX Runtime' see
<https://onnxruntime.ai/>.

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
