%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  readnoaa
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Access 'NOAA' Climate and Weather Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.6.0
BuildRequires:    R-CRAN-httr2 >= 1.0.0
BuildRequires:    R-tools 
Requires:         R-CRAN-cli >= 3.6.0
Requires:         R-CRAN-httr2 >= 1.0.0
Requires:         R-tools 

%description
Provides clean, tidy access to climate and weather data from the 'National
Oceanic and Atmospheric Administration' ('NOAA') via the 'National Centers
for Environmental Information' ('NCEI') Data Service API
<https://www.ncei.noaa.gov/access/services/data/v1>. Covers daily weather
observations, monthly and annual summaries, and 30-year climate normals
from over 100,000 stations across 180 countries. No API key is required.
Dedicated functions handle the most common datasets, while a generic
fetcher provides access to all 'NCEI' datasets. Station discovery
functions help users find stations by location or name. Data is downloaded
on first use and cached locally for subsequent calls. This package is not
endorsed or certified by 'NOAA'.

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
