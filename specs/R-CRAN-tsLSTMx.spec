%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tsLSTMx
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Predict Time Series Using LSTM Model Including Exogenous Variable to Denote Zero Values

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-tensorflow 
BuildRequires:    R-CRAN-AllMetrics 
BuildRequires:    R-CRAN-keras 
BuildRequires:    R-CRAN-reticulate 
Requires:         R-CRAN-tensorflow 
Requires:         R-CRAN-AllMetrics 
Requires:         R-CRAN-keras 
Requires:         R-CRAN-reticulate 

%description
It is a versatile tool for predicting time series data using Long
Short-Term Memory (LSTM) models. It is specifically designed to handle
time series with an exogenous variable, allowing users to denote whether
data was available for a particular period or not. The package encompasses
various functionalities, including hyperparameter tuning, custom loss
function support, model evaluation, and one-step-ahead forecasting. With
an emphasis on ease of use and flexibility, it empowers users to explore,
evaluate, and deploy LSTM models for accurate time series predictions and
forecasting in diverse applications. More details can be found in Garai
and Paul (2023) <doi:10.1016/j.iswa.2023.200202>.

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
