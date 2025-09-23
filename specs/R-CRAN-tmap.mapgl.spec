%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tmap.mapgl
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Extensions to 'tmap' with Two New Modes: 'mapbox' and 'maplibre'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-tmap >= 4.2
BuildRequires:    R-CRAN-mapgl >= 0.4
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-stars 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-tmaptools 
BuildRequires:    R-CRAN-units 
Requires:         R-CRAN-tmap >= 4.2
Requires:         R-CRAN-mapgl >= 0.4
Requires:         R-CRAN-terra 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-stars 
Requires:         R-CRAN-data.table 
Requires:         R-grDevices 
Requires:         R-CRAN-colorspace 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-tmaptools 
Requires:         R-CRAN-units 

%description
The 'tmap' package provides two plotting modes for static and interactive
thematic maps. This package extends 'tmap' with two additional modes based
on 'Mapbox GL JS' and 'MapLibre GL JS'. These modes feature interactive
vector tiles, globe views, and other modern web-mapping capabilities,
while maintaining a consistent 'tmap' interface across all plotting modes.

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
