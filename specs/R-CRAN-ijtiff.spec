%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ijtiff
%global packver   3.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Comprehensive TIFF I/O with Full Support for 'ImageJ' TIFF Files

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    libjpeg-turbo-devel
BuildRequires:    libtiff-devel
BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildRequires:    R-CRAN-checkmate >= 1.9.3
BuildRequires:    R-CRAN-fs >= 1.5
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-strex >= 1.5
BuildRequires:    R-CRAN-stringr >= 1.4
BuildRequires:    R-CRAN-rlang >= 1.0
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-imager 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-zeallot 
Requires:         R-CRAN-checkmate >= 1.9.3
Requires:         R-CRAN-fs >= 1.5
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-strex >= 1.5
Requires:         R-CRAN-stringr >= 1.4
Requires:         R-CRAN-rlang >= 1.0
Requires:         R-CRAN-cli 
Requires:         R-CRAN-dplyr 
Requires:         R-graphics 
Requires:         R-CRAN-imager 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-lubridate 
Requires:         R-methods 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-zeallot 

%description
General purpose TIFF file I/O for R users.  Currently the only such
package with read and write support for TIFF files with floating point
(real-numbered) pixels, and the only package that can correctly import
TIFF files that were saved from 'ImageJ' and write TIFF files than can be
correctly read by 'ImageJ' <https://imagej.net/ij/>. Also supports text
image I/O.

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
