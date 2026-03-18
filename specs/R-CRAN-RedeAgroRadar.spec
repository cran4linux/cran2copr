%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RedeAgroRadar
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Weather Radar Monitoring and 'Telegram' Alerts for Agriculture Research

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-magick 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-bslib 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-magick 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-bslib 

%description
Provides tools to download, process, and analyze real-time meteorological
radar images from Simepar (Paraná, Brazil)
<https://www.simepar.br/simepar/radar_msc>. Designed to support the 'Rede
Agropesquisa' hydrological monitoring, it includes functions to detect
rainfall intensity based on Red, Green, and Blue (RGB) color values within
predefined circular study areas. Features automated integration with the
'Telegram Bot API' <https://core.telegram.org/bots/api> to send
spatialized image alerts and an interactive 'shiny' dashboard for easy
configuration and continuous weather tracking.

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
