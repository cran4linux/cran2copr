%global __brp_check_rpaths %{nil}
%global packname  ASIP
%global packver   0.4.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.9
Release:          3%{?dist}%{?buildtag}
Summary:          Automated Satellite Image Processing

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-raster >= 2.6.7
BuildRequires:    R-CRAN-rgdal >= 1.2.16
BuildRequires:    R-CRAN-stringr >= 1.2.0
BuildRequires:    R-utils 
Requires:         R-CRAN-raster >= 2.6.7
Requires:         R-CRAN-rgdal >= 1.2.16
Requires:         R-CRAN-stringr >= 1.2.0
Requires:         R-utils 

%description
Efficiently perform complex satellite image processes automatically with
minimum inputs. Functions are providing more control on the user to
specify how the function needs to be executed by offering more
customization options and facilitate more functionalities. The functions
are designed to identify the type of input satellite images and perform
accordingly. Also, some functions are giving options to perform multiple
satellite data (even from different types) in single run. Package
currently supports satellite images from most widely used Landsat 4,5,7
and 8 and Sentinel-2 MSI data. The primary applications of this package
are given below. 1. Conversion of optical bands to top of atmosphere
reflectance. 2. Conversion of thermal bands to corresponding temperature
images. 3. Derive application oriented products directly from source
satellite image bands. 4. Compute user defined equation and produce
corresponding image product. 5. Other basic tools for satellite image
processing. REFERENCES. i. Chander and Markham (2003)
<doi:10.1109/TGRS.2003.818464>. ii. Roy et.al, (2014)
<doi:10.1016/j.rse.2014.02.001>. iii. Abrams (2000)
<doi:10.1080/014311600210326>.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
