%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  shinyglass
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Liquid Glass Design Themes for 'shiny' Applications

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny >= 1.5.0
BuildRequires:    R-CRAN-bslib >= 0.5.0
BuildRequires:    R-CRAN-htmltools >= 0.5.0
BuildRequires:    R-CRAN-sass >= 0.4.0
Requires:         R-CRAN-shiny >= 1.5.0
Requires:         R-CRAN-bslib >= 0.5.0
Requires:         R-CRAN-htmltools >= 0.5.0
Requires:         R-CRAN-sass >= 0.4.0

%description
Provides drop-in Liquid Glass themes for 'shiny'. Call glass_theme() and
pass the result as theme = to fluidPage(), navbarPage(), or any
'bslib'-aware page function to get translucent surfaces, backdrop blur,
and system typography on 'Bootstrap' components. Includes light and dark
presets with runtime switching and an OS-following 'auto' mode, an
iOS-style intensity control from Ultra Clear to Tinted
(glass_intensity_slider()), and options for accent color, blur, corner
radius, and motion or tint behavior.

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
