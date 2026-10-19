%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  forecastsuite
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Multi-Model Time Series Forecasting Toolkit and Local App

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-shinycssloaders 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-colourpicker 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-shinycssloaders 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-colourpicker 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-grDevices 
Requires:         R-graphics 

%description
Fits, compares and visualizes univariate time series forecasts through an
extensible model registry built largely on the 'forecast' package:
AutoRegressive Integrated Moving Average (ARIMA) and Seasonal ARIMA
(SARIMA) models (Hyndman and Khandakar (2008)
<doi:10.18637/jss.v027.i03>), Error, Trend, Seasonal (ETS) exponential
smoothing (Hyndman et al. (2002) <doi:10.1016/S0169-2070(01)00110-8>),
Trigonometric seasonality, Box-Cox transformation, AutoRegressive Moving
Average (ARMA) errors, Trend and Seasonal components (TBATS) models (De
Livera, Hyndman and Snyder (2011) <doi:10.1198/jasa.2011.tm09771>), Neural
Network AutoRegression (NNETAR) and Holt-Winters exponential smoothing
(Winters (1960) <doi:10.1287/mnsc.6.3.324>), plus optional 'Prophet'
models via the 'prophet' package (Taylor and Letham (2018)
<doi:10.1080/00031305.2017.1380080>) and Long Short-Term Memory (LSTM)
networks via the 'torch' package (Hochreiter and Schmidhuber (1997)
<doi:10.1162/neco.1997.9.8.1735>). Also provides grouped series with
bottom-up and top-down reconciliation, rolling-origin cross-validation,
ensembles and residual diagnostics, following Hyndman and Athanasopoulos
(2021) <https://otexts.com/fpp3/>, and a bundled local 'shiny' application
exposing every model.

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
