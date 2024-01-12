%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  trackeR
%global packver   1.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.0
Release:          1%{?dist}%{?buildtag}
Summary:          Infrastructure for Running, Cycling and Swimming Data from GPS-Enabled Tracking Devices

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggridges 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-RSQLite 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-scam 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-fda 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-leaflet 
BuildRequires:    R-CRAN-ggmap 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-gtable 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggridges 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-RSQLite 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-scam 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-fda 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-leaflet 
Requires:         R-CRAN-ggmap 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-gtable 

%description
Provides infrastructure for handling running, cycling and swimming data
from GPS-enabled tracking devices within R. The package provides methods
to extract, clean and organise workout and competition data into
session-based and unit-aware data objects of class 'trackeRdata' (S3
class). The information can then be visualised, summarised, and analysed
through flexible and extensible methods. Frick and Kosmidis (2017) <doi:
10.18637/jss.v082.i07>, which is updated and maintained as one of the
vignettes, provides detailed descriptions of the package and its methods,
and real-data demonstrations of the package functionality.

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
