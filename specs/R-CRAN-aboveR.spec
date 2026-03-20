%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  aboveR
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          'LiDAR' Terrain Analysis and Change Detection from Above

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lidR 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-CRAN-sf 
Requires:         R-CRAN-lidR 
Requires:         R-CRAN-terra 
Requires:         R-CRAN-sf 

%description
Terrain change detection, cut and fill volume estimation, terrain
profiling, reclamation monitoring, erosion analysis, and flood risk
assessment from 'LiDAR' (Light Detection and Ranging) point clouds and
digital elevation models ('DEMs'). Applications include surface mine
reclamation monitoring, sediment pond capacity tracking, highwall safety
classification, and erosion channel detection. Built on 'lidR' for point
cloud I/O and 'terra' for raster operations. Includes access utilities for
'KyFromAbove' cloud-native elevation data on Amazon Web Services ('AWS')
<https://kyfromabove.ky.gov/>. Methods for terrain change detection and
volume estimation follow Li and others (2005)
<doi:10.1016/j.geomorph.2004.10.007>.

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
