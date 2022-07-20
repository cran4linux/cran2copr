%global __brp_check_rpaths %{nil}
%global packname  lidaRtRee
%global packver   4.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Forest Analysis with Airborne Laser Scanning (LiDAR) Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lidR >= 4.0.0
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-imager 
BuildRequires:    R-CRAN-leaps 
BuildRequires:    R-CRAN-gvlma 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-reldist 
Requires:         R-CRAN-lidR >= 4.0.0
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-grDevices 
Requires:         R-CRAN-terra 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-imager 
Requires:         R-CRAN-leaps 
Requires:         R-CRAN-gvlma 
Requires:         R-CRAN-car 
Requires:         R-CRAN-reldist 

%description
Provides functions for forest analysis using airborne laser scanning
(LiDAR remote sensing) data: tree detection (method 1 in Eysn et al.
(2015) <doi:10.3390/f6051721>) and segmentation; forest parameters
estimation and mapping with the area-based approach. It includes
complementary steps for forest mapping: co-registration of field plots
with LiDAR data (Monnet and Mermin (2014) <doi:10.3390/f5092307>);
extraction of both physical (gaps, edges, trees) and statistical features
from LiDAR data useful for e.g. habitat suitability modeling (Glad et al.
(2020) <doi:10.1002/rse2.117>) and forest maturity mapping (Fuhr et al.
(2022) <doi:10.1002/rse2.274>); model calibration with ground reference,
and maps export.

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
