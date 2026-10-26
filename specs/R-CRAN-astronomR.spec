%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  astronomR
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Cosmic Insights: Statistical Frameworks for Astronomers

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-stringr >= 1.5.0
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-stringr >= 1.5.0
Requires:         R-CRAN-httr 
Requires:         R-CRAN-jsonlite 
Requires:         R-stats 
Requires:         R-CRAN-tibble 

%description
A comprehensive toolkit for astronomical and cosmological computations.
Provides functions for angular coordinate conversions (degrees,
hours-minutes-seconds, degrees-minutes-seconds, and radians), Julian Days
and the conversion of equatorial (right ascension, declination) to
horizontal (altitude, azimuth) coordinates, access to fundamental physical
constants ('CODATA' 2018), queries to the Gaia Catalogue of Nearby Stars
through the Gaia Archive TAP (Table Access Protocol) service, a
'Lambda-CDM' cosmology model with comoving, luminosity and
angular-diameter distances, cosmic time and the age of the universe,
early-universe thermal physics including photon density, 'Saha' equation
solutions, and a full thermal-cosmology module covering the Hubble rate in
the radiation-dominated era, effective relativistic degrees of freedom,
entropy density, equilibrium yields, the Boltzmann relic-abundance
('pebble') equation for WIMP freeze-out, the freeze-out temperature
solver, and the Peebles equation for hydrogen recombination. Also includes
the Drake equation for estimating the number of communicating
extraterrestrial civilisations in the Milky Way.

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
