%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  EEAaq
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Handle Air Quality Data from the European Environmental Agency Data Portal

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-gstat 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-leaflet 
BuildRequires:    R-CRAN-tictoc 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-mondate 
BuildRequires:    R-CRAN-aweek 
BuildRequires:    R-CRAN-ggspatial 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-gstat 
Requires:         R-grDevices 
Requires:         R-CRAN-leaflet 
Requires:         R-CRAN-tictoc 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-mondate 
Requires:         R-CRAN-aweek 
Requires:         R-CRAN-ggspatial 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 

%description
This software downloads and manages air quality data at the European level
from the European Environmental Agency (EEA) dataflows
(<https://www.eea.europa.eu/data-and-maps/data/aqereporting-9>). The
package allows dynamically mapping the stations, summarising and time
aggregating the measurements and building spatial interpolation maps. See
the webpage <https://www.eea.europa.eu/en> for further information on
EEA's activities and history.

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
