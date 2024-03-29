%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  drugDemand
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Drug Demand Forecasting

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-MASS >= 7.3.54
BuildRequires:    R-CRAN-plotly >= 4.10.1
BuildRequires:    R-parallel >= 4.1.2
BuildRequires:    R-stats >= 3.5.0
BuildRequires:    R-CRAN-nlme >= 3.1.153
BuildRequires:    R-CRAN-survival >= 2.41.3
BuildRequires:    R-CRAN-doRNG >= 1.8.6
BuildRequires:    R-CRAN-foreach >= 1.5.2
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-mvtnorm >= 1.1.3
BuildRequires:    R-CRAN-dplyr >= 1.1.0
BuildRequires:    R-CRAN-rlang >= 1.1.0
BuildRequires:    R-CRAN-purrr >= 1.0.2
BuildRequires:    R-CRAN-doParallel >= 1.0.17
BuildRequires:    R-CRAN-Rcpp >= 1.0.10
BuildRequires:    R-CRAN-L1pack >= 0.41.24
BuildRequires:    R-CRAN-erify >= 0.4.0
BuildRequires:    R-CRAN-eventPred >= 0.2.3
Requires:         R-CRAN-MASS >= 7.3.54
Requires:         R-CRAN-plotly >= 4.10.1
Requires:         R-parallel >= 4.1.2
Requires:         R-stats >= 3.5.0
Requires:         R-CRAN-nlme >= 3.1.153
Requires:         R-CRAN-survival >= 2.41.3
Requires:         R-CRAN-doRNG >= 1.8.6
Requires:         R-CRAN-foreach >= 1.5.2
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-mvtnorm >= 1.1.3
Requires:         R-CRAN-dplyr >= 1.1.0
Requires:         R-CRAN-rlang >= 1.1.0
Requires:         R-CRAN-purrr >= 1.0.2
Requires:         R-CRAN-doParallel >= 1.0.17
Requires:         R-CRAN-Rcpp >= 1.0.10
Requires:         R-CRAN-L1pack >= 0.41.24
Requires:         R-CRAN-erify >= 0.4.0
Requires:         R-CRAN-eventPred >= 0.2.3

%description
Performs drug demand forecasting by modeling drug dispensing data while
taking into account predicted enrollment and treatment discontinuation
dates. The gap time between randomization and the first drug dispensing
visit is modeled using interval-censored exponential, Weibull,
log-logistic, or log-normal distributions (Anderson-Bergman (2017)
<doi:10.18637/jss.v081.i12>). The number of skipped visits is modeled
using Poisson, zero-inflated Poisson, or negative binomial distributions
(Zeileis, Kleiber & Jackman (2008) <doi:10.18637/jss.v027.i08>). The gap
time between two consecutive drug dispensing visits given the number of
skipped visits is modeled using linear regression based on least squares
or least absolute deviations (Birkes & Dodge (1993, ISBN:0-471-56881-3)).
The number of dispensed doses is modeled using linear or linear
mixed-effects models (McCulloch & Searle (2001, ISBN:0-471-19364-X)).

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
