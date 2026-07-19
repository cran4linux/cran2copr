%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  potentiomap
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Build Potentiometric Surfaces and Hydraulic-Gradient Arrows

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-gstat 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-CRAN-xml2 
Requires:         R-CRAN-fields 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-CRAN-gstat 
Requires:         R-CRAN-sf 
Requires:         R-stats 
Requires:         R-CRAN-terra 
Requires:         R-CRAN-xml2 

%description
Prepares groundwater-level observations from measured hydraulic head or
from depth-to-water and land-surface elevation, interpolates
potentiometric surfaces using thin-plate splines, inverse-distance
weighting, ordinary Kriging, universal Kriging, or user-supplied methods,
and creates raster, contour, diagnostic, support, and hydraulic-gradient
products for review and export. Functions retain method conditions and fit
diagnostics, validate explicit prediction tasks, inspect model-conditional
uncertainty and monitoring-network sensitivity, identify limited
prediction support, and check whether scaled hydraulic-gradient arrows
remain within finite raster support and end at lower modeled head. Raster
processing uses methods from 'terra' (Hijmans 2025)
<doi:10.32614/CRAN.package.terra>, thin-plate splines use methods from
'fields' (Nychka et al. 2021) <doi:10.5065/D6W957CT>, and geostatistical
interpolation uses methods from 'gstat' (Pebesma 2004)
<doi:10.1016/j.cageo.2004.03.012>.

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
