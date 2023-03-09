%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  meteoForecast
%global packver   0.56
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.56
Release:          1%{?dist}%{?buildtag}
Summary:          Numerical Weather Predictions

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-ncdf4 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-XML 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-ncdf4 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-XML 

%description
Access to several Numerical Weather Prediction services both in raster
format and as a time series for a location. Currently it works with GFS
<https://www.ncei.noaa.gov/products/weather-climate-models/global-forecast>,
MeteoGalicia
<https://www.meteogalicia.gal/web/modelos/threddsIndex.action>, NAM
<https://www.ncei.noaa.gov/products/weather-climate-models/north-american-mesoscale>,
and RAP
<https://www.ncei.noaa.gov/products/weather-climate-models/rapid-refresh-update>.

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
