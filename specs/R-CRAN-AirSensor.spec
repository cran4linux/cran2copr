%global __brp_check_rpaths %{nil}
%global packname  AirSensor
%global packver   1.0.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.8
Release:          1%{?dist}%{?buildtag}
Summary:          Process and Display Data from Air Quality Sensors

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-PWFSLSmoke >= 1.2.111
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-worldmet >= 0.9.2
BuildRequires:    R-CRAN-MazamaSpatialUtils >= 0.7.3
BuildRequires:    R-CRAN-MazamaCoreUtils >= 0.4.6
BuildRequires:    R-CRAN-MazamaLocationUtils >= 0.1.13
BuildRequires:    R-CRAN-countrycode 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-dygraphs 
BuildRequires:    R-CRAN-geodist 
BuildRequires:    R-CRAN-geosphere 
BuildRequires:    R-CRAN-GGally 
BuildRequires:    R-CRAN-ggmap 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-httpcode 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-leaflet 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-openair 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-seismicRoll 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-CRAN-zoo 
Requires:         R-CRAN-PWFSLSmoke >= 1.2.111
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-worldmet >= 0.9.2
Requires:         R-CRAN-MazamaSpatialUtils >= 0.7.3
Requires:         R-CRAN-MazamaCoreUtils >= 0.4.6
Requires:         R-CRAN-MazamaLocationUtils >= 0.1.13
Requires:         R-CRAN-countrycode 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-dygraphs 
Requires:         R-CRAN-geodist 
Requires:         R-CRAN-geosphere 
Requires:         R-CRAN-GGally 
Requires:         R-CRAN-ggmap 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-httpcode 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-leaflet 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-openair 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-seismicRoll 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-xts 
Requires:         R-CRAN-zoo 

%description
Process and display data from air quality sensors. Initial focus is on
PM2.5 measurements from sensors produced by 'PurpleAir'
<https://www2.purpleair.com>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
