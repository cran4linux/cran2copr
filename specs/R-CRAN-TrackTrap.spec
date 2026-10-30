%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  TrackTrap
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Calculate and Visualize Degree-Days for Pest Monitoring

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-daymetr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-tools 
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-daymetr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-magrittr 
Requires:         R-utils 
Requires:         R-CRAN-rlang 
Requires:         R-tools 

%description
Combines pest trap observations with daily temperatures to calculate and
visualize cumulative degree-days. Temperature inputs include 'Daymet'
<https://daymet.ornl.gov>, 'Open-Meteo' <https://open-meteo.com/>, reports
from the California Irrigation Management Information System ('CIMIS')
<https://cimis.water.ca.gov>, and user-supplied daily weather data.
Degree-days are calculated using the simple-average method with either an
upper threshold applied to the daily mean or an explicitly selected
calculation without an upper cutoff. The first positive trap count defines
the biofix for every pest, with accumulation beginning on the following
day. Negative daily degree-day values are set to zero. Users can provide
temperature thresholds and optional thermal reference values. Thermal
reference markers and their multiples do not independently establish
flight or generation identities. Complete daily calculations and weather
provenance are retained with the output to support reproducibility.

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
