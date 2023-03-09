%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  hydflood
%global packver   0.5.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.3
Release:          1%{?dist}%{?buildtag}
Summary:          Flood Extents and Durations along the Rivers Elbe and Rhine

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-hyd1d 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-terra 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-hyd1d 
Requires:         R-stats 
Requires:         R-CRAN-Rdpack 
Requires:         R-grDevices 

%description
Raster based flood modelling internally using 'hyd1d', an R package to
interpolate 1d water level and gauging data. The package computes flood
extent and durations through strategies originally developed for 'INFORM',
an 'ArcGIS'-based hydro-ecological modelling framework. It does not
provide a full, physical hydraulic modelling algorithm, but a simplified,
near real time 'GIS' approach for flood extent and duration modelling.
Computationally demanding annual flood durations have been computed
already and data products were published by Weber (2022)
<doi:10.1594/PANGAEA.948042>.

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
