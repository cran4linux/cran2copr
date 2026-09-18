%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  arimasel
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Cartesian Product-Based ARIMA Model Identification and Selection

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
BuildRequires:    R-parallel 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-utils 
Requires:         R-parallel 

%description
Provides an alternative algorithm for ARIMA and seasonal ARIMA model
identification based on Cartesian products of user-supplied parameter
sets. Rather than relying on ACF/PACF plots or stepwise search (as in
auto.arima()), the package exhaustively evaluates every candidate
(p,d,q)(P,D,Q)[m] combination in the requested index sets, ranks all
converged models by AIC, AICc, BIC, and HQIC simultaneously, computes
Akaike weights for model uncertainty quantification, supports exogenous
regressors, produces ensemble forecasts, evaluates candidate models by
rolling-origin (expanding window) cross-validation, and provides
publication-quality diagnostic and comparison plots. A feature-based
exploratory data analysis suite computes scale-free time series
characteristics (trend and seasonal strength, spectral entropy,
autocorrelation, lumpiness, stability) in the spirit of Hyndman, Wang and
Laptev (2015), and a feature-guided automatic search narrows the Cartesian
product model space before the exhaustive search runs. The algorithm is
flexible, transparent, and widely applicable for quick, reproducible ARIMA
model selection in both academic research and industry forecasting
pipelines. Applications are demonstrated with Nigerian macroeconomic time
series data.

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
