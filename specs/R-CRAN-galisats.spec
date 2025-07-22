%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  galisats
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Configuration of Jupiter's Four Largest Satellites

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-png 
Requires:         R-graphics 
Requires:         R-CRAN-png 

%description
Calculate and plot the configuration of Jupiter's four largest satellites
(known as Galilean satellites) for a given date and time (ET - Ephemeris
Time). The 'galsat' function returns numerical values of the satellites’
positions. x – the apparent rectangular coordinate of the satellite with
respect to the center of Jupiter’s disk in the equatorial plane in the
units of Jupiter’s equatorial radius; X is positive toward the west, y –
the apparent rectangular coordinate of the satellite with respect to the
center of Jupiter’s disk from the equatorial plane in the units of
Jupiter’s equatorial radius; Y is positive toward the north. For more
details see Meeus (1988, ISBN 0-943396-22-0) "Astronomical Formulae for
Calculators".

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
