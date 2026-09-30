%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  qpmR
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Quarterly Projection Models for Monetary Policy Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-QZ 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-QZ 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-tools 
Requires:         R-utils 

%description
An end-to-end implementation of the semi-structural quarterly projection
models used in central-bank forecasting and policy analysis systems: model
declaration with model-consistent expectations, a generalized Schur solver
with Blanchard-Kahn diagnostics following Klein (2000)
<doi:10.1016/S0165-1889(99)00045-7>, Kalman filtering and smoothing for
latent states such as the output gap and the neutral rate, historical
shock decompositions, conditional forecasts that distinguish announced
from unanticipated policy paths, an auditable judgment ledger, forecast
rounds with revision decompositions, Bayesian estimation with
identification diagnostics following Iskrev (2010)
<doi:10.1016/j.jmoneco.2009.12.007>, and reporting. The canonical small
open economy model of Berg, Karam and Laxton (2006)
<doi:10.5089/9781451863413.001> ships as a calibrated template, with
extension blocks for disaggregated food inflation and managed exchange
rates.

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
