%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  QUALYPSO
%global packver   3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Partitioning Uncertainty Components of an Incomplete Ensemble of Climate Projections

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-expm 
BuildRequires:    R-CRAN-Rfast 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-gamlss 
BuildRequires:    R-CRAN-gamlss.dist 
BuildRequires:    R-CRAN-statmod 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-expm 
Requires:         R-CRAN-Rfast 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-gamlss 
Requires:         R-CRAN-gamlss.dist 
Requires:         R-CRAN-statmod 

%description
These functions apply an analysis of variance to incomplete ensembles of
climate projections. It provides estimates of climate change responses of
all simulation chains and of all uncertainty variables. It has been
applied to different ensembles of projections simulated to study the
impact of climate change: for climate indicators in Evin et al. (2019)
<doi:10.1175/JCLI-D-18-0606.1>; seasonal precipitation and temperature in
Evin, Somot and Hingray (2021) <doi:10.5194/esd-12-1543-2021>;
hydrological variables in Evin et al. (2026)
<doi:10.5194/hess-30-1023-2026>; photovoltaic energy in Bichet et al.
(2019) <doi:10.1088/1748-9326/ab500a>.

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
