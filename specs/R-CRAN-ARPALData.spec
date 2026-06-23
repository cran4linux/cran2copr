%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ARPALData
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Retrieving and Analyzing Air Quality and Weather Data from ARPA Lombardia

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tm 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-eurostat 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-aweek 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-CRAN-httr2 
BuildRequires:    R-CRAN-jsonlite 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-dplyr 
Requires:         R-utils 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tm 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-eurostat 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-aweek 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-future 
Requires:         R-CRAN-future.apply 
Requires:         R-CRAN-httr2 
Requires:         R-CRAN-jsonlite 

%description
Contains functions for retrieving, managing, and analyzing air quality and
weather data from the Regione Lombardia open database
(<https://www.dati.lombardia.it/>). Data are collected by ARPA Lombardia
(Lombardia Environmental Protection Agency), Italy, through its ground
monitoring network (<https://www.dati.lombardia.it/stories/s/auv9-c2sj>).
See the website <https://www.arpalombardia.it/> for further information on
ARPA Lombardia's activities and history. Data quality (e.g., missing
values, extreme values, and graphical mapping) has been checked in
collaboration with members of ARPA Lombardia's air quality control office.
The package provides observations since 1989 (for weather) and 1968 (for
air quality), and these data are updated daily by the regional agency. A
full description of the package is available in the companion paper
Maranzano & Algieri (2024), "ARPALData: an R package for retrieving and
analyzing air quality and weather data from ARPA Lombardia (Italy)",
Environmental and Ecological Statistics, <doi:10.1007/s10651-024-00599-6>.

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
