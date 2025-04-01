%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tsaux
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Time Series Forecasting Auxiliary Functions

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tsmethods 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-scoringRules 
BuildRequires:    R-CRAN-stlplus 
BuildRequires:    R-CRAN-tsoutliers 
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-data.table 
Requires:         R-CRAN-tsmethods 
Requires:         R-methods 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-xts 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-car 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-scoringRules 
Requires:         R-CRAN-stlplus 
Requires:         R-CRAN-tsoutliers 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-data.table 

%description
A suite of auxiliary functions that enhance time series estimation and
forecasting, including a robust anomaly detection routine based on Chen
and Liu (1993) <doi:10.2307/2290724> (imported and wrapped from the
'tsoutliers' package), utilities for managing calendar and time
conversions, performance metrics to assess both point forecasts and
distributional predictions, advanced simulation by allowing the generation
of time series components—such as trend, seasonal, ARMA, irregular, and
anomalies—in a modular fashion based on the innovations form of the state
space model and a number of transformation methods including Box-Cox,
Logit, 'Softplus-Logit' and Sigmoid.

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
