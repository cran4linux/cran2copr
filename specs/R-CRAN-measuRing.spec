%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  measuRing
%global packver   0.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.1
Release:          1%{?dist}%{?buildtag}
Summary:          Detection and Control of Tree-Ring Widths on Scanned Image Sections

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-pastecs 
BuildRequires:    R-CRAN-png 
BuildRequires:    R-CRAN-tiff 
BuildRequires:    R-CRAN-dplR 
Requires:         R-CRAN-pastecs 
Requires:         R-CRAN-png 
Requires:         R-CRAN-tiff 
Requires:         R-CRAN-dplR 

%description
Identification of ring borders on scanned image sections from
dendrochronological samples. Processing of image reflectances to produce
gray matrices and time series of smoothed gray values. Luminance data is
plotted on segmented images for users to perform both: visual
identification of ring borders or control of automatic detection. Routines
to visually include/exclude ring borders on the R graphical devices, or
automatically detect ring borders using a linear detection algorithm. This
algorithm detects ring borders according to positive/negative extreme
values in the smoothed time-series of gray values. Most of the in-package
routines can be recursively implemented using the multiDetect() function.

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
