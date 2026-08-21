%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  TrackTrap
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Model Cumulative Growing Degree-Days for Pest Monitoring

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-daymetr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-degday 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-daymetr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-degday 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-magrittr 
Requires:         R-utils 
Requires:         R-CRAN-rlang 

%description
Pest monitoring is crucial, especially during the early season, to
understand the distribution and the proliferation of the target pest. Raw
count data from pest monitoring/traps can be coupled with derived
environmental variables such as growing degree-day ('GDD') to get useful
insights about the pest phenology. This package pulls temperature data
from the 'Daymet' application programming interface ('API',
<https://daymet.ornl.gov>), or 'Open-Meteo' ('API',
<https://open-meteo.com/>) or manual user-supplied CSV file from the
California Irrigation Management Information System ('CIMIS',
<https://cimis.water.ca.gov>), for a user-specified time period and
calculates cumulative growing degree-days. Users provide intended date
range, pest of concern, and the geographic coordinates of the trap
location to track pest emergence and phenology throughout the growing
season.

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
