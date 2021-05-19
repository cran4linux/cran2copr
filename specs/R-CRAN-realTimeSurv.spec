%global packname  realTimeSurv
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Real Time Disease Surveillance Using Geospatial Statistical Modelling

License:          CC BY-SA 4.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-lgcp >= 1.7
BuildRequires:    R-CRAN-ncdf4 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-rgeos 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-googleway 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-maptools 
BuildRequires:    R-CRAN-spatstat.geom 
BuildRequires:    R-CRAN-geoR 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-kableExtra 
BuildRequires:    R-CRAN-geosphere 
BuildRequires:    R-CRAN-ggspatial 
BuildRequires:    R-CRAN-spatstat 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-bayesplot 
Requires:         R-CRAN-lgcp >= 1.7
Requires:         R-CRAN-ncdf4 
Requires:         R-methods 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-rgeos 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-googleway 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-maptools 
Requires:         R-CRAN-spatstat.geom 
Requires:         R-CRAN-geoR 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-kableExtra 
Requires:         R-CRAN-geosphere 
Requires:         R-CRAN-ggspatial 
Requires:         R-CRAN-spatstat 
Requires:         R-parallel 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-bayesplot 

%description
Convenient tools and data for the real-time surveillance of infectious
disease and various visualisation and reporting tools. The package serves
as a wrapper to a variety of geostatistical ('lgcp', 'sp', 'rgeos', etc.)
and plotting packages ('ggplot2', 'ggmap', 'ggspatial', etc. ) for R, and
is intended to enable rapid deployment of real-time surveillance
statistical software.

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
