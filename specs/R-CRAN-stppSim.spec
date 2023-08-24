%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  stppSim
%global packver   1.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.1
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
BuildRequires:    R-CRAN-otuSummary 
BuildRequires:    R-CRAN-progressr 
BuildRequires:    R-CRAN-future.apply 
Requires:         R-CRAN-splancs 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-sf 
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
Requires:         R-CRAN-otuSummary 
Requires:         R-CRAN-progressr 
Requires:         R-CRAN-future.apply 

%description
Generates artificial spatiotemporal (ST) point patterns and/or
interactions through the integration of microsimulation (Holm, E.,
(2017)<doi:10.1002/9781118786352.wbieg0320>) and agent-based models
(Bonabeau, E., (2002)<doi:10.1073/pnas.082080899>). The tool enables users
to configure the actions of a group of 'walkers', which can be agents,
objects, individuals, and more. Their engagements with both spatial
landscapes (Quaglietta, L. and Porto, M.,
(2019)<doi:10.1186/s40462-019-0154-8>) and time domains result in specific
spatiotemporal point patterns and/or interactions. These emerging
spatiotemporal patterns can be visualized, analyzed, and then employed for
both spatial and temporal model assessments. Given the growing scarcity of
detailed spatiotemporal data, this package offers an alternative dataset
for a broad spectrum of studies in both the social and life sciences.

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
