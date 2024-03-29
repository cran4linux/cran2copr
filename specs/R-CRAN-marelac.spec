%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  marelac
%global packver   2.1.11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.11
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for Aquatic Sciences

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildRequires:    R-CRAN-shape 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-seacarb 
Requires:         R-CRAN-shape 
Requires:         R-stats 
Requires:         R-CRAN-seacarb 

%description
Datasets, constants, conversion factors, and utilities for 'MArine',
'Riverine', 'Estuarine', 'LAcustrine' and 'Coastal' science. The package
contains among others: (1) chemical and physical constants and datasets,
e.g. atomic weights, gas constants, the earths bathymetry; (2) conversion
factors (e.g. gram to mol to liter, barometric units, temperature,
salinity); (3) physical functions, e.g. to estimate concentrations of
conservative substances, gas transfer and diffusion coefficients, the
Coriolis force and gravity; (4) thermophysical properties of the seawater,
as from the UNESCO polynomial or from the more recent derivation based on
a Gibbs function.

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
