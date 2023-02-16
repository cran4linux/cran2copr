%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PoolDilutionR
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Calculate Gross Biogeochemical Flux Rates from Isotope Pool Dilution Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch

%description
Pool dilution is a isotope tracer technique wherein a biogeochemical pool
is artifically enriched with its heavy isotopologue and the gross
productive and consumptive fluxes of that pool are quantified by the
change in pool size and isotopic composition over time. This package
calculates gross production and consumption rates from closed-system
isotopic pool dilution time series data. Pool size concentrations and
heavy isotope (e.g., 15N) content are measured over time and the model
optimizes production rate (P) and the first order rate constant (k) by
minimizing error in the model-predicted total pool size, as well as the
isotopic signature. The model optimizes rates by weighting information
against the signal:noise ratio of concentration and heavy- isotope
signatures using measurement precision as well as the magnitude of change
over time. The calculations used here are based on von Fischer and Hedin
(2002) <doi:10.1029/2001GB001448> with some modifications.

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
