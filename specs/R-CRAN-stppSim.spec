%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  stppSim
%global packver   1.2.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.7
Release:          1%{?dist}%{?buildtag}
Summary:          Spatiotemporal Point Patterns Simulation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-splancs 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-ks 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-SiMRiv 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-spatstat.geom 
BuildRequires:    R-CRAN-sparr 
BuildRequires:    R-CRAN-chron 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-geosphere 
BuildRequires:    R-CRAN-leaflet 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-gstat 
Requires:         R-CRAN-splancs 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-ks 
Requires:         R-CRAN-terra 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-SiMRiv 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-spatstat.geom 
Requires:         R-CRAN-sparr 
Requires:         R-CRAN-chron 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-geosphere 
Requires:         R-CRAN-leaflet 
Requires:         R-methods 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-gstat 

%description
Generates artificial spatiotemporal (ST) point patterns through the
integration of microsimulation (Holm, E.,
(2017)<doi:10.1002/9781118786352.wbieg0320>) and agent-based models
(Bonabeau, E., (2002)<doi:10.1073/pnas.082080899>). Allows a user to
define the behaviours of a set of 'walkers' (agents, objects, persons,
etc.) whose interactions with the spatial (landscape) (Quaglietta, L. and
Porto, M., (2019)<doi:10.1186/s40462-019-0154-8>) and the temporal domains
produce new point events. The resulting ST patterns from the point cloud
can be measured and utilized for spatial and/or temporal model testings
and evaluations. Application: With increasingly limited availability of
fine-grained spatially and temporally stamped point data, the package
provides an alternative source of data for a wide range of research in
social and life sciences.

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
