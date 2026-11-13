%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  msarima
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Multi-Seasonal ARIMA Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-polynom 
BuildRequires:    R-stats 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-polynom 
Requires:         R-stats 

%description
Fit, forecast and simulate autoregressive integrated moving average
(ARIMA) models with more than one seasonal component, following Lisi and
Grigoletto (2025) <doi:10.1002/for.3283>. Series observed at high
frequency often display several seasonal cycles at once, such as the daily
and the weekly pattern of hourly data, which a single seasonal ARIMA
operator cannot represent. Estimation is performed by conditional maximum
likelihood through numerical optimisation, with support for fixed
coefficients and a constant term. Multi-seasonal Ljung-Box and Monti
portmanteau tests, following Grigoletto and Lisi (2026)
<doi:10.48550/arXiv.2609.32381>, seasonal correlograms, forecasts with
prediction intervals, and simulation from a model specification or from a
fitted model are also provided.

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
