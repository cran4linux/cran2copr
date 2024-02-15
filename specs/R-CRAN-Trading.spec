%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Trading
%global packver   3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0
Release:          1%{?dist}%{?buildtag}
Summary:          CCR, Advanced Correlation & Beta Estimates, Betting Strategies

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-reticulate 
BuildRequires:    R-CRAN-PerformanceAnalytics 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-RcppAlgos 
Requires:         R-methods 
Requires:         R-CRAN-reticulate 
Requires:         R-CRAN-PerformanceAnalytics 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-RcppAlgos 

%description
Contains performance analysis metrics of track records including
entropy-based correlation and dynamic beta based on the Kalman filter. The
normalized sample entropy method has been implemented which produces
accurate entropy estimation even on smaller datasets while for the dynamic
beta calculation the Kalman filter methodology has been utilized. On a
separate stream, trades from the five major assets classes and also
functionality to use pricing curves, rating tables, CSAs and add-on
tables. The implementation follows an object oriented logic whereby each
trade inherits from more abstract classes while also the curves/tables are
objects. Furthermore, odds calculators and P&L back-testing functionality
has been implemented for the most widely used betting/trading strategies
including martingale, DAlembert, Labouchere and Fibonacci. Back-testing
has also been included for the EuroMillions and EuroJackpot lotteries.
Furthermore, some basic functionality about climate risk has been
included.

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
