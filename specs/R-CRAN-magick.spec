%global packname  magick
%global packver   2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1
Release:          1%{?dist}
Summary:          Advanced Graphics and Image-Processing in R

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    ImageMagick-c++-devel
Requires:         ImageMagick-c++
BuildRequires:    R-devel
Requires:         R-core
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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/images
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
