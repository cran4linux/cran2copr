%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  imager
%global packver   0.42.14
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.42.14
Release:          1%{?dist}%{?buildtag}
Summary:          Image Processing Library Based on 'CImg'

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    fftw-devel
BuildRequires:    libtiff-devel
BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildRequires:    R-CRAN-Rcpp >= 0.11.5
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-png 
BuildRequires:    R-CRAN-jpeg 
BuildRequires:    R-CRAN-readbitmap 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-downloader 
BuildRequires:    R-CRAN-igraph 
Requires:         R-CRAN-Rcpp >= 0.11.5
Requires:         R-CRAN-magrittr 
Requires:         R-methods 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-png 
Requires:         R-CRAN-jpeg 
Requires:         R-CRAN-readbitmap 
Requires:         R-grDevices 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-downloader 
Requires:         R-CRAN-igraph 

%description
Fast image processing for images in up to 4 dimensions (two spatial
dimensions, one time/depth dimension, one colour dimension). Provides most
traditional image processing tools (filtering, morphology,
transformations, etc.) as well as various functions for easily analysing
image data using R. The package wraps 'CImg', <http://cimg.eu>, a simple,
modern C++ library for image processing.

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
