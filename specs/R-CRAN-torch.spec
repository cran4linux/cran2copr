%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  torch
%global packver   0.12.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.12.0
Release:          1%{?dist}%{?buildtag}
Summary:          Tensors and Neural Networks with 'GPU' Acceleration

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-cli >= 3.0.0
BuildRequires:    R-CRAN-coro >= 1.0.2
BuildRequires:    R-CRAN-safetensors >= 0.1.1
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-withr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-bit64 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-callr 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-ellipsis 
BuildRequires:    R-CRAN-desc 
BuildRequires:    R-CRAN-jsonlite 
Requires:         R-CRAN-cli >= 3.0.0
Requires:         R-CRAN-coro >= 1.0.2
Requires:         R-CRAN-safetensors >= 0.1.1
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-withr 
Requires:         R-CRAN-rlang 
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-CRAN-bit64 
Requires:         R-CRAN-magrittr 
Requires:         R-tools 
Requires:         R-CRAN-callr 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-ellipsis 
Requires:         R-CRAN-desc 
Requires:         R-CRAN-jsonlite 

%description
Provides functionality to define and train neural networks similar to
'PyTorch' by Paszke et al (2019) <arXiv:1912.01703> but written entirely
in R using the 'libtorch' library. Also supports low-level tensor
operations and 'GPU' acceleration.

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
