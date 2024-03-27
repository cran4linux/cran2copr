%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sarima
%global packver   0.9.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.3
Release:          1%{?dist}%{?buildtag}
Summary:          Simulation and Prediction with Seasonal ARIMA Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-PolynomF >= 1.0.0
BuildRequires:    R-CRAN-lagged >= 0.2.1
BuildRequires:    R-CRAN-Rcpp >= 0.12.14
BuildRequires:    R-methods 
BuildRequires:    R-stats4 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-ltsa 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-PolynomF >= 1.0.0
Requires:         R-CRAN-lagged >= 0.2.1
Requires:         R-CRAN-Rcpp >= 0.12.14
Requires:         R-methods 
Requires:         R-stats4 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-ltsa 

%description
Functions, classes and methods for time series modelling with ARIMA and
related models. The aim of the package is to provide consistent interface
for the user. For example, a single function autocorrelations() computes
various kinds of theoretical and sample autocorrelations. This is work in
progress, see the documentation and vignettes for the current
functionality.  Function sarima() fits extended multiplicative seasonal
ARIMA models with trends, exogenous variables and arbitrary roots on the
unit circle, which can be fixed or estimated (for the algebraic basis for
this see <arXiv:2208.05055>, a paper on the methodology is being
prepared).

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
