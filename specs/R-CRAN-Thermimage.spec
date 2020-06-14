%global packname  Thermimage
%global packver   4.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.0.1
Release:          2%{?dist}
Summary:          Thermal Image Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         perl(Image::ExifTool)
Requires:         ImageMagick
BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-tiff 
BuildRequires:    R-CRAN-png 
Requires:         R-CRAN-tiff 
Requires:         R-CRAN-png 

%description
A collection of functions and routines for inputting thermal image video
files, plotting and converting binary raw data into estimates of
temperature.  First published 2015-03-26.  Written primarily for research
purposes in biological applications of thermal images.  v1 included the
base calculations for converting thermal image binary values to
temperatures. v2 included additional equations for providing heat transfer
calculations and an import function for thermal image files (v2.2.3 fixed
error importing thermal image to windows OS). v3. Added numerous functions
for converting thermal image, videos, rewriting and exporting. v3.1. Added
new functions to convert files. v3.2.  Fixed the various functions related
to finding frame times. v4.0. fixed an error in atmospheric attenuation
constants, affecting raw2temp and temp2raw functions. Recommend update for
use with long distance calculations.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/exiftool
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/perl
%{rlibdir}/%{packname}/INDEX
