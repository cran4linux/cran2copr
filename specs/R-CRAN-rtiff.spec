%global packname  rtiff
%global packver   1.4.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.8
Release:          1%{?dist}%{?buildtag}
Summary:          Read and Write TIFF Files

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    libtiff-devel
BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-pixmap 
Requires:         R-CRAN-pixmap 

%description
Reads and writes TIFF format images and returns them as a pixmap object.
Because the resulting object can be very large for even modestly sized
TIFF images, images can be reduced as they are read for improved
performance.  This package is a wrapper around libtiff (www.libtiff.org),
on which it depends (i.e. the libtiff shared library must be on your PATH
for the binary to work, and tiffio.h must be on your system to build the
package from source). By using libtiff's highlevel TIFFReadRGBAImage
function, this package inherently supports a wide range of image formats
and compression schemes. This package also provides an implementation of
the Ridler Autothresholding algorithm for easy generation of binary masks
as described in Ridler & Calvard (1978) <doi:10.1109/TSMC.1978.4310039>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
