%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  palettecore
%global packver   0.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.1
Release:          1%{?dist}%{?buildtag}
Summary:          Derive, Optimise and Audit a Scientific Colour Palette from One Seed Colour

License:          Apache License (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-stats 
Requires:         R-utils 

%description
Generates sequential, diverging and categorical colour palettes from a
single seed colour in OKLCH (the cylindrical lightness-chroma-hue
representation of the Oklab perceptual colour space), with spacing
measured by the CIEDE2000 colour-difference formula of the International
Commission on Illumination. Audits every palette under simulated
colour-vision deficiency, greyscale conversion, the standard Red Green
Blue (sRGB) gamut and Web Content Accessibility Guidelines (WCAG)
contrast. Colour-vision deficiency is simulated at severity 1.0 with the
model of Machado, Oliveira and Fernandes (2009)
<doi:10.1109/TVCG.2009.113>; the design rationale follows Crameri,
Shephard and Heron (2020) <doi:10.1038/s41467-020-19160-7>. Mirrors the
'Python' reference implementation maintained in the same repository and is
validated against shared parity fixtures. Thresholds are configurable
design rules, not established accessibility cut-offs.

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
