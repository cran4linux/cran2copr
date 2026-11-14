%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  vantorr
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Access 'Maxar' and 'Vantor' Satellite Imagery APIs

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-httr2 
BuildRequires:    R-CRAN-sf 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-httr2 
Requires:         R-CRAN-sf 

%description
Provides a client for the 'Maxar' and 'Vantor' 'REST' and 'OGC' APIs
(<https://developers.maxar.com/docs/>), enabling programmatic access to
high-resolution satellite imagery (such as 'WorldView', 'Vivid' base maps,
and analysis-ready data). Includes functions for 'OAuth2' and API key
authentication, discovery and 'STAC' catalog search, 'OGC' web services
('WMS', 'WMTS', 'WFS'), survey fieldwork resource generation (printable
field atlases, index grids, 'Survey Solutions' and 'ODK' assignment
tables, offline 'GeoPackage' and 'Esri' tile packages), interactive
'leaflet' and 'shiny' application modules, and spatial data retrieval
integrated with 'sf', 'terra', and 'stars'.

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
