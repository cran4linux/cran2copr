%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  magick
%global packver   2.8.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.8.7
Release:          1%{?dist}%{?buildtag}
Summary:          Advanced Graphics and Image-Processing in R

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    ImageMagick-c++-devel
BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.12
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-curl 
Requires:         R-CRAN-Rcpp >= 0.12.12
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-curl 

%description
Bindings to 'ImageMagick': the most comprehensive open-source image
processing library available. Supports many common formats (png, jpeg,
tiff, pdf, etc) and manipulations (rotate, scale, crop, trim, flip, blur,
etc). All operations are vectorized via the Magick++ STL meaning they
operate either on a single frame or a series of frames for working with
layers, collages, or animation. In RStudio images are automatically
previewed when printed to the console, resulting in an interactive editing
environment. The latest version of the package includes a native graphics
device for creating in-memory graphics or drawing onto images using pixel
coordinates.

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
