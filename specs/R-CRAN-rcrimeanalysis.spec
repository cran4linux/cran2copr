%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rcrimeanalysis
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          1%{?dist}%{?buildtag}
Summary:          An Implementation of Crime Analysis Methods

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-ggmap 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-leaflet 
BuildRequires:    R-CRAN-leafsync 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-KernSmooth 
BuildRequires:    R-CRAN-pals 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-terra 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-ggmap 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-leaflet 
Requires:         R-CRAN-leafsync 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-KernSmooth 
Requires:         R-CRAN-pals 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-sp 
Requires:         R-stats 
Requires:         R-CRAN-terra 

%description
An implementation of functions for the analysis of crime incident or
records management system data. The package implements analysis algorithms
scaled for city or regional crime analysis units. The package provides
functions for kernel density estimation for crime heat maps, geocoding
using the 'Google Maps' API, identification of repeat crime incidents,
spatio-temporal map comparison across time intervals, time series analysis
(forecasting and decomposition), detection of optimal parameters for the
identification of near repeat incidents, and near repeat analysis with
crime network linkage.

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
