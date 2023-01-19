%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  LWFBrook90R
%global packver   0.5.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.2
Release:          1%{?dist}%{?buildtag}
Summary:          Simulate Evapotranspiration and Soil Moisture with the SVAT Model LWF-Brook90

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-foreach >= 1.5.0
BuildRequires:    R-CRAN-parallelly >= 1.30.0
BuildRequires:    R-CRAN-future >= 1.19.0
BuildRequires:    R-CRAN-data.table >= 1.10.4
BuildRequires:    R-CRAN-iterators >= 1.0.12
BuildRequires:    R-CRAN-progressr >= 0.6.0
BuildRequires:    R-CRAN-vegperiod >= 0.3.0
BuildRequires:    R-CRAN-doFuture >= 0.10.0
BuildRequires:    R-methods 
Requires:         R-CRAN-foreach >= 1.5.0
Requires:         R-CRAN-parallelly >= 1.30.0
Requires:         R-CRAN-future >= 1.19.0
Requires:         R-CRAN-data.table >= 1.10.4
Requires:         R-CRAN-iterators >= 1.0.12
Requires:         R-CRAN-progressr >= 0.6.0
Requires:         R-CRAN-vegperiod >= 0.3.0
Requires:         R-CRAN-doFuture >= 0.10.0
Requires:         R-methods 

%description
Provides a flexible and easy-to use interface for the soil vegetation
atmosphere transport (SVAT) model LWF-BROOK90, written in Fortran. The
model simulates daily transpiration, interception, soil and snow
evaporation, streamflow and soil water fluxes through a soil profile
covered with vegetation, as described in Hammel & Kennel (2001,
ISBN:978-3-933506-16-0) and Federer et al. (2003)
<doi:10.1175/1525-7541(2003)004%%3C1276:SOAETS%%3E2.0.CO;2>. A set of
high-level functions for model set up, execution and parallelization
provides easy access to plot-level SVAT simulations, as well as multi-run
and large-scale applications.

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
