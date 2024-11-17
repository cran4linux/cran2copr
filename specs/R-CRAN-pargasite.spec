%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pargasite
%global packver   2.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Pollution-Associated Risk Geospatial Analysis Site

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-sf >= 1.0.15
BuildRequires:    R-CRAN-stars >= 0.6.5
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-gstat 
BuildRequires:    R-CRAN-leaflet 
BuildRequires:    R-CRAN-leafsync 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-raqs 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinycssloaders 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-sf >= 1.0.15
Requires:         R-CRAN-stars >= 0.6.5
Requires:         R-CRAN-cli 
Requires:         R-CRAN-gstat 
Requires:         R-CRAN-leaflet 
Requires:         R-CRAN-leafsync 
Requires:         R-methods 
Requires:         R-CRAN-raqs 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinycssloaders 
Requires:         R-stats 
Requires:         R-utils 

%description
Offers tools to estimate and visualize levels of major pollutants (CO,
NO2, SO2, Ozone, PM2.5 and PM10) across the conterminous United States for
user-defined time ranges. Provides functions to retrieve pollutant data
from the U.S. Environmental Protection Agency’s 'Air Quality System' (AQS)
API service <https://aqs.epa.gov/aqsweb/documents/data_api.html> for
interactive visualization through a 'shiny' application, allowing users to
explore pollutant levels for a given location over time relative to the
National Ambient Air Quality Standards (NAAQS).

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
