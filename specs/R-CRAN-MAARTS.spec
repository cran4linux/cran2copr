%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MAARTS
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Merger and Acquisition Autoregressive Time-Series Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-tseries 
BuildRequires:    R-CRAN-urca 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-CRAN-nortest 
BuildRequires:    R-CRAN-moments 
BuildRequires:    R-CRAN-strucchange 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-numDeriv 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-tseries 
Requires:         R-CRAN-urca 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-utils 
Requires:         R-CRAN-lmtest 
Requires:         R-CRAN-sandwich 
Requires:         R-CRAN-nortest 
Requires:         R-CRAN-moments 
Requires:         R-CRAN-strucchange 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-numDeriv 

%description
Implements comprehensive Merger and Acquisition ('M&A') Autoregressive
('AR') time-series models with full statistical analysis capabilities. The
package provides parameter estimation, forecasting with confidence
intervals (80%%, 90%%, 95%%, 99%%), descriptive statistics, stationarity tests
(Augmented Dickey-Fuller ('ADF'), Phillips-Perron,
Kwiatkowski-Phillips-Schmidt-Shin ('KPSS'), Dickey-Fuller Generalized
Least Squares ('DF-GLS')), autocorrelation analysis (Autocorrelation
Function ('ACF'), Partial Autocorrelation Function ('PACF')), model
diagnostics (Ljung-Box, Box-Pierce), accuracy measures (Mean Squared Error
('MSE'), Mean Absolute Error ('MAE'), Mean Absolute Scaled Error ('MASE'),
Root Mean Squared Error ('RMSE'), Symmetric Mean Absolute Percentage Error
('SMAPE'), F-statistic), residual diagnostics (normality tests,
heteroscedasticity tests), model stability analysis, impulse response,
information criteria (Akaike Information Criterion ('AIC'), Bayesian
Information Criterion ('BIC'), Hannan-Quinn Information Criterion
('HQIC')), structural break analysis, spectral analysis, and Monte Carlo
simulation. Models are based on: Kumar, Mudassir, and Agiwal (2024)
<https://ph02.tci-thaijo.org/index.php/thaistat/article/view/253436>,
Kumar, Mudassir, and Srivastava (2025) <doi:10.1007/s44199-025-00104-3>,
Kumar and Mudassir (2025) <doi:10.19139/soic-2310-5070-2029>.

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
