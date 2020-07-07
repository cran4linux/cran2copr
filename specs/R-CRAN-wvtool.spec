%global packname  wvtool
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}
Summary:          Image Tools for Automated Wood Identification

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch

%description
This tool, wood vision tool, is intended to facilitate preprocessing and
analyzing 2-dimensional wood images toward automated recognition. The
former includes some basics such as functions to RGB to grayscale, gray to
binary, cropping, rotation(bilinear), median/mean/Gaussian filter, and
Canny/Sobel edge detection. The latter includes gray level co-occurrence
matrix (GLCM), Haralick parameters, local binary pattern (LBP), higher
order local autocorrelation (HLAC), Fourier transform (radial and
azimuthal integration), and Gabor filtering. The functions are intended to
read data using 'readTIFF(x,info=T)' from 'tiff' package. The functions in
this packages basically assumes the grayscale images as input data, thus
the color images should be subjected to the function rgb2gray() before
used for some other functions.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
