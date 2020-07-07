%global packname  imager
%global packver   0.42.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.42.3
Release:          3%{?dist}
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

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%doc %{rlibdir}/%{packname}/NEWS
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/include
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
