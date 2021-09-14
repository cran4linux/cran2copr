%global __brp_check_rpaths %{nil}
%global packname  masscor
%global packver   0.0.7.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.7.1
Release:          1%{?dist}%{?buildtag}
Summary:          Mass Measurement Corrections

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-metRology 
Requires:         R-CRAN-metRology 

%description
Mass measurement corrections and uncertainties using calibration data, as
recommended by EURAMET's guideline No. 18 (2015) ISBN:978-3-942992-40-4 .
The package provides classes, functions, and methods for storing
information contained in calibration certificates and converting balance
readings to both conventional mass and real mass. For the latter, the
Magnitude of the Air Buoyancy Correction factor employs models (such as
the CIMP-2007 formula revised by Picard, Davis, Gläser, and Fujii (2008)
<doi:10.1088/0026-1394/45/2/004>) to estimate the local air density using
measured environmental conditions.

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
