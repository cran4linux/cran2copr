%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  forecastHybrid
%global packver   5.1.21
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          5.1.21
Release:          1%{?dist}%{?buildtag}
Summary:          Convenient Functions for Ensemble Time Series Forecasts

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.4
Requires:         R-core >= 4.0.4
BuildArch:        noarch
BuildRequires:    R-CRAN-forecast >= 8.16
BuildRequires:    R-CRAN-ggplot2 >= 3.3.6
BuildRequires:    R-CRAN-zoo >= 1.8
BuildRequires:    R-CRAN-foreach >= 1.5.1
BuildRequires:    R-CRAN-doParallel >= 1.0.16
BuildRequires:    R-CRAN-purrr >= 0.3.5
BuildRequires:    R-CRAN-thief 
Requires:         R-CRAN-forecast >= 8.16
Requires:         R-CRAN-ggplot2 >= 3.3.6
Requires:         R-CRAN-zoo >= 1.8
Requires:         R-CRAN-foreach >= 1.5.1
Requires:         R-CRAN-doParallel >= 1.0.16
Requires:         R-CRAN-purrr >= 0.3.5
Requires:         R-CRAN-thief 

%description
Convenient functions for ensemble forecasts in R combining approaches from
the 'forecast' package. Forecasts generated from auto.arima(), ets(),
thetaf(), nnetar(), stlm(), tbats(), snaive() and arfima() can be combined
with equal weights, weights based on in-sample errors (introduced by Bates
& Granger (1969) <doi:10.1057/jors.1969.103>), or cross-validated weights.
Cross validation for time series data with user-supplied models and
forecasting functions is also supported to evaluate model accuracy.

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
