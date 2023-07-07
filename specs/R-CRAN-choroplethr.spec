%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  choroplethr
%global packver   3.7.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.7.2
Release:          1%{?dist}%{?buildtag}
Summary:          Simplify the Creation of Choropleth Maps in R

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 2.0.0
BuildRequires:    R-CRAN-tigris >= 1.0
BuildRequires:    R-CRAN-acs 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-WDI 
BuildRequires:    R-CRAN-ggmap 
BuildRequires:    R-CRAN-RgoogleMaps 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-rvest 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-tidycensus 
Requires:         R-CRAN-ggplot2 >= 2.0.0
Requires:         R-CRAN-tigris >= 1.0
Requires:         R-CRAN-acs 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-WDI 
Requires:         R-CRAN-ggmap 
Requires:         R-CRAN-RgoogleMaps 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-rvest 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-tidycensus 

%description
Choropleths are thematic maps where geographic regions, such as states,
are colored according to some metric, such as the number of people who
live in that state. This package simplifies this process by 1. Providing
ready-made functions for creating choropleths of common maps. 2. Providing
data and API connections to interesting data sources for making
choropleths. 3. Providing a framework for creating choropleths from
arbitrary shapefiles. 4. Overlaying those maps over reference maps from
Google Maps.

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
