%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Rvcg
%global packver   0.22.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.22.2
Release:          1%{?dist}%{?buildtag}
Summary:          Manipulations of Triangular Meshes Based on the 'VCGLIB' API

License:          GPL (>= 2) | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RcppEigen 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-utils 

%description
Operations on triangular meshes based on 'VCGLIB'. This package integrates
nicely with the R-package 'rgl' to render the meshes processed by 'Rvcg'.
The Visualization and Computer Graphics Library (VCG for short) is an open
source portable C++ templated library for manipulation, processing and
displaying with OpenGL of triangle and tetrahedral meshes. The library,
composed by more than 100k lines of code, is released under the GPL
license, and it is the base of most of the software tools of the Visual
Computing Lab of the Italian National Research Council Institute ISTI
<https://vcg.isti.cnr.it/>, like 'metro' and 'MeshLab'. The 'VCGLIB'
source is pulled from trunk <https://github.com/cnr-isti-vclab/vcglib> and
patched to work with options determined by the configure script as well as
to work with the header files included by 'RcppEigen'.

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
