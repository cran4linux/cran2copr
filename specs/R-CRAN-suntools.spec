%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  suntools
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Calculate Sun Position, Sunrise, Sunset, Solar Noon and Twilight

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-stats 
Requires:         R-methods 
Requires:         R-CRAN-sf 
Requires:         R-stats 

%description
Provides a set of convenient functions for calculating sun-related
information, including the sun's position (elevation and azimuth), and the
times of sunrise, sunset, solar noon, and twilight for any given
geographical location on Earth. These calculations are based on equations
provided by the National Oceanic & Atmospheric Administration (NOAA)
<https://gml.noaa.gov/grad/solcalc/calcdetails.html> as described in
"Astronomical Algorithms" by Jean Meeus (1991, ISBN: 978-0-943396-35-4). A
resource for researchers and professionals working in fields such as
climatology, biology, and renewable energy.

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
