%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rNOMADS
%global packver   2.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.5.1
Release:          1%{?dist}%{?buildtag}
Summary:          An R Interface to the NOAA Operational Model Archive and Distribution System

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-fields >= 9.0
BuildRequires:    R-CRAN-XML >= 3.99.0.3
BuildRequires:    R-CRAN-GEOmap >= 2.3.5
BuildRequires:    R-CRAN-httr >= 1.4.4
BuildRequires:    R-CRAN-stringr >= 1.2.0
BuildRequires:    R-CRAN-rvest >= 0.3.2
BuildRequires:    R-CRAN-uuid >= 0.1.2
BuildRequires:    R-CRAN-MBA 
Requires:         R-CRAN-fields >= 9.0
Requires:         R-CRAN-XML >= 3.99.0.3
Requires:         R-CRAN-GEOmap >= 2.3.5
Requires:         R-CRAN-httr >= 1.4.4
Requires:         R-CRAN-stringr >= 1.2.0
Requires:         R-CRAN-rvest >= 0.3.2
Requires:         R-CRAN-uuid >= 0.1.2
Requires:         R-CRAN-MBA 

%description
An interface to the National Oceanic and Atmospheric Administration's
Operational Model Archive and Distribution System (NOMADS, see
<https://nomads.ncep.noaa.gov/> for more information) that allows R users
to quickly and efficiently download global and regional weather model data
for processing.  rNOMADS currently supports a variety of models ranging
from global weather data to an altitude of over 40 km, to high resolution
regional weather models, to wave and sea ice models.  rNOMADS can retrieve
binary data in grib format as well as import ascii data directly into R by
interfacing with the GrADS-DODS system.

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
