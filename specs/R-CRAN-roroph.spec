%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  roroph
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Philippine Roll-on/Roll-Off (RoRo) Connectivity and Transport Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ArchipelagoEngine 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-spdep 
Requires:         R-CRAN-ArchipelagoEngine 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-spdep 

%description
Provides the first standardized dataset of the Philippines'
Roll-on/Roll-off (RoRo) shipping network, reflecting the 2024-2026
operational state. It digitizes fragmented records from the Maritime
Industry Authority (MARINA) and Philippine Ports Authority (PPA) into a
unified framework for transport modeling. The package includes 108
bidirectional provincial links across the Western, Central, and Eastern
Nautical Highways, complete with GADM-standardized naming, geospatial
coordinates, and metrics such as distance, travel time, and vessel
frequency. Methodology follows Anselin (1988, ISBN:9024737354) and LeSage
and Pace (2009) <doi:10.1201/9781420064254> for spatial weight
construction. Data sources include "MARINA Inventory of RoRo Routes"
<https://marina.gov.ph> and "PPA Port Statistics"
<https://www.ppa.com.ph/ppa_statistics>. Designed to support research in
economic geography and disaster-response logistics.

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
