%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PlanetNICFI
%global packver   1.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.5
Release:          1%{?dist}%{?buildtag}
Summary:          Processing of the 'Planet NICFI' Satellite Imagery

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Recommends:       aria2
BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-terra 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-glue 
Requires:         R-utils 
Requires:         R-CRAN-terra 

%description
It includes functions to download and process the 'Planet NICFI' (Norway's
International Climate and Forest Initiative) Satellite Imagery utilizing
the Planet Mosaics API
<https://developers.planet.com/docs/basemaps/reference/#tag/Basemaps-and-Mosaics>.
'GDAL' (library for raster and vector geospatial data formats) and
'aria2c' (paralleled download utility) must be installed and configured in
the user's Operating System.

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
