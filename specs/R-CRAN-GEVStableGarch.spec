%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  GEVStableGarch
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          ARMA-GARCH/APARCH Models with Stable, GEV and GAt Innovations

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-libstable4u 
BuildRequires:    R-CRAN-Rsolnp 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-libstable4u 
Requires:         R-CRAN-Rsolnp 
Requires:         R-stats 
Requires:         R-utils 

%description
Simulation, estimation and forecasting of autoregressive moving average
(ARMA) models with generalized autoregressive conditional
heteroskedasticity (GARCH) or asymmetric power ARCH (APARCH, with ARCH the
autoregressive conditional heteroskedasticity model) errors, with stable
(S0 parametrization), generalized extreme value (GEV) and generalized
asymmetric t (GAt) innovations. The innovation distribution is a pluggable
object, so user defined densities get the same fitting, simulation,
stationarity and forecasting machinery.

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
