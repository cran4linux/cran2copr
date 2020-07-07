%global packname  rtiff
%global packver   1.4.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.7
Release:          3%{?dist}
Summary:          Read and Write TIFF Files

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    libtiff-devel
Requires:         libtiff
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


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/tiff
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
