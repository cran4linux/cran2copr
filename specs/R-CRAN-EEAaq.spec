%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  EEAaq
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Handle Air Quality Data from the European Environment Agency Data Portal

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-arrow 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-gifski 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-gstat 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-leaflet 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-ggspatial 
Requires:         R-CRAN-arrow 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-gifski 
Requires:         R-grDevices 
Requires:         R-CRAN-gstat 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-leaflet 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-sf 
Requires:         R-stats 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-utils 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-ggspatial 

%description
This software downloads and manages air quality data from the European
Environmental Agency (EEA) dataflow
(<https://www.eea.europa.eu/data-and-maps/data/aqereporting-9>). See the
web page <https://eeadmz1-downloads-webapp.azurewebsites.net/> for details
on the EEA's Air Quality Download Service. The package allows dynamically
mapping the stations, summarising and time aggregating the measurements
and building spatial interpolation maps. See the web page
<https://www.eea.europa.eu/en> for further information on EEA activities
and history. Further details, as well as, an extended vignette of the main
functions included in the package, are available at the GitHub web page
dedicated to the project.

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
