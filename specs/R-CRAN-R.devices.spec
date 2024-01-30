%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  R.devices
%global packver   2.17.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.17.2
Release:          1%{?dist}%{?buildtag}
Summary:          Unified Handling of Graphics Devices

License:          LGPL (>= 2.1)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.0
Requires:         R-core >= 2.14.0
BuildArch:        noarch
BuildRequires:    R-CRAN-R.utils >= 2.10.1
BuildRequires:    R-CRAN-R.methodsS3 >= 1.8.1
BuildRequires:    R-CRAN-R.oo >= 1.24.0
BuildRequires:    R-CRAN-base64enc >= 0.1.2
BuildRequires:    R-grDevices 
Requires:         R-CRAN-R.utils >= 2.10.1
Requires:         R-CRAN-R.methodsS3 >= 1.8.1
Requires:         R-CRAN-R.oo >= 1.24.0
Requires:         R-CRAN-base64enc >= 0.1.2
Requires:         R-grDevices 

%description
Functions for creating plots and image files in a unified way regardless
of output format (EPS, PDF, PNG, SVG, TIFF, WMF, etc.). Default device
options as well as scales and aspect ratios are controlled in a uniform
way across all device types. Switching output format requires minimal
changes in code. This package is ideal for large-scale batch processing,
because it will never leave open graphics devices or incomplete image
files behind, even on errors or user interrupts.

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
