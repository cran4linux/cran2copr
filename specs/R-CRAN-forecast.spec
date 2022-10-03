%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  forecast
%global packver   8.18
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          8.18
Release:          1%{?dist}%{?buildtag}
Summary:          Forecasting Functions for Time Series and Linear Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-ggplot2 >= 2.2.1
BuildRequires:    R-CRAN-RcppArmadillo >= 0.2.35
BuildRequires:    R-CRAN-Rcpp >= 0.11.0
BuildRequires:    R-CRAN-generics >= 0.1.2
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-fracdiff 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-nnet 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-timeDate 
BuildRequires:    R-CRAN-tseries 
BuildRequires:    R-CRAN-urca 
BuildRequires:    R-CRAN-zoo 
Requires:         R-CRAN-ggplot2 >= 2.2.1
Requires:         R-CRAN-Rcpp >= 0.11.0
Requires:         R-CRAN-generics >= 0.1.2
Requires:         R-CRAN-colorspace 
Requires:         R-CRAN-fracdiff 
Requires:         R-graphics 
Requires:         R-CRAN-lmtest 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-nnet 
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-CRAN-timeDate 
Requires:         R-CRAN-tseries 
Requires:         R-CRAN-urca 
Requires:         R-CRAN-zoo 

%description
Methods and tools for displaying and analysing univariate time series
forecasts including exponential smoothing via state space models and
automatic ARIMA modelling.

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
