%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ECTSVR
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Error Correction Term Based Support Vector Regression for Time Series

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-urca 
BuildRequires:    R-CRAN-tseries 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-Metrics 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-CRAN-urca 
Requires:         R-CRAN-tseries 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-Metrics 
Requires:         R-CRAN-knitr 
Requires:         R-stats 
Requires:         R-graphics 

%description
The cointegration based support vector regression model is a combination
of error correction model and support vector regression. This hybrid model
allows the researcher to make use of the information extracted by the
cointegrating vector as an input in the support vector regression mode.
Implements the models with multiple kernel functions (linear, polynomial,
radial, sigmoid) for time series forecasting. Includes stationarity tests,
Johansen cointegration, and comprehensive model evaluation.

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
