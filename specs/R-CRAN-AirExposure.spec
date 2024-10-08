%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  AirExposure
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Exposure Model to Air Pollutants Based on Mobility and Daily Activities

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.1
Requires:         R-core >= 4.1.1
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-leaflet 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-sf 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-leaflet 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-sf 

%description
Model that assesses daily exposure to air pollution, which considers daily
population mobility on a geographical scale and the spatial and temporal
variability of pollutant concentrations, in addition to traditional
parameters such as exposure time and pollutant concentration.

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
