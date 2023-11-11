%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  GLCMTextures
%global packver   0.3.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.9
Release:          1%{?dist}%{?buildtag}
Summary:          GLCM Textures of Raster Layers

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-terra 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-raster 

%description
Calculates grey level co-occurrence matrix (GLCM) based texture measures
(Hall-Beyer (2017)
<https://prism.ucalgary.ca/bitstream/handle/1880/51900/texture%%20tutorial%%20v%%203_0%%20180206.pdf>;
Haralick et al. (1973) <doi:10.1109/TSMC.1973.4309314>) of raster layers
using a sliding rectangular window. It also includes functions to quantize
a raster into grey levels as well as tabulate a glcm and calculate glcm
texture metrics for a matrix.

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
