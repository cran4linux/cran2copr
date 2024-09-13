%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  GSODR
%global packver   4.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Global Surface Summary of the Day ('GSOD') Weather Data Client

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table >= 1.15.4
BuildRequires:    R-CRAN-countrycode 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-R.utils 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-withr 
Requires:         R-CRAN-data.table >= 1.15.4
Requires:         R-CRAN-countrycode 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-R.utils 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-withr 

%description
Provides automated downloading, parsing, cleaning, unit conversion and
formatting of Global Surface Summary of the Day ('GSOD') weather data from
the from the USA National Centers for Environmental Information ('NCEI').
Units are converted from from United States Customary System ('USCS')
units to International System of Units ('SI').  Stations may be
individually checked for number of missing days defined by the user, where
stations with too many missing observations are omitted.  Only stations
with valid reported latitude and longitude values are permitted in the
final data.  Additional useful elements, saturation vapour pressure
('es'), actual vapour pressure ('ea') and relative humidity ('RH') are
calculated from the original data using the improved August-Roche-Magnus
approximation (Alduchov & Eskridge 1996) and included in the final data
set.  The resulting metadata include station identification information,
country, state, latitude, longitude, elevation, weather observations and
associated flags.  For information on the 'GSOD' data from 'NCEI', please
see the 'GSOD' 'readme.txt' file available from,
<https://www1.ncdc.noaa.gov/pub/data/gsod/readme.txt>.

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
