%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gdi
%global packver   1.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.1
Release:          1%{?dist}%{?buildtag}
Summary:          Volumetric Analysis using Graphic Double Integration

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-jpeg 
BuildRequires:    R-CRAN-png 
Requires:         R-CRAN-jpeg 
Requires:         R-CRAN-png 

%description
Tools implementing an automated version of the graphic double integration
technique first employed by Jerison (1973) <ISBN:9780323141086> and
Hurlburt (1999) <doi:10.1080/02724634.1999.10011145>. Graphic double
integration is primarily used for volume or mass estimation of (extinct)
animals, and the package 'gdi' aims to make this technique as convenient
and versatile as possible. The main functions of 'gdi' provide utilities
for automatically measuring diameters from digital silhouettes provided as
image files, and for calculating volume via graphic double integration
with a simple elliptical, superelliptical (following Motani 2001
<doi:10.1666/0094-8373(2001)027%%3C0735:EBMFST%%3E2.0.CO;2>) or complex
cross-sectional model. Additionally, the package contains functions to
help with estimating the position of the center of mass (COM), and for
visualizing results.

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
