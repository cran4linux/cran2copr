%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  WaveST
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Wavelet-Based Spatial Time Series Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-neuralnet 
BuildRequires:    R-CRAN-tsutils 
BuildRequires:    R-CRAN-wavelets 
Requires:         R-CRAN-forecast 
Requires:         R-stats 
Requires:         R-CRAN-neuralnet 
Requires:         R-CRAN-tsutils 
Requires:         R-CRAN-wavelets 

%description
An integrated wavelet-based spatial time series modelling framework
designed to enhance predictive accuracy under noisy and nonstationary
conditions by jointly exploiting multi-resolution (wavelet) information
and spatial dependence. The package implements WaveSARIMA() (Wavelet Based
Spatial AutoRegressive Integrated Moving Average model using regression
features with forecast::auto.arima()) and WaveSNN() (Wavelet Based Spatial
Neural Network model using neuralnet with hyperparameter search). Both
functions support spatial transformation via a user-supplied spatial
matrix, lag feature construction, MODWT-based wavelet sub-series feature
generation, time-ordered train/test splitting, and performance evaluation
(Root Mean Square Error (RMSE), Mean Absolute Error (MAE), R-squared (R²),
and Mean Absolute Percentage Error (MAPE)), returning fitted models and
actual vs predicted values for train and test sets. The package has been
developed using the algorithm of Paul et al. (2023)
<doi:10.1007/s43538-025-00581-1>.

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
