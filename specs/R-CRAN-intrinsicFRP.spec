%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  intrinsicFRP
%global packver   2.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          An R Package for Factor Model Asset Pricing

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-glmnet 
Requires:         R-graphics 
Requires:         R-CRAN-Rcpp 

%description
Functions for evaluating and testing asset pricing models, including
estimation and testing of factor risk premia, selection of "strong" risk
factors (factors having nonzero population correlation with test asset
returns), heteroskedasticity and autocorrelation robust covariance matrix
estimation and testing for model misspecification and identification. The
functions for estimating and testing factor risk premia implement the
Fama-MachBeth (1973) <doi:10.1086/260061> two-pass approach, the
misspecification-robust approaches of Kan-Robotti-Shanken (2013)
<doi:10.1111/jofi.12035>, and the approaches based on tradable factor risk
premia of Quaini-Trojani-Yuan (2023) <doi:10.2139/ssrn.4574683>. The
functions for selecting the "strong" risk factors are based on the Oracle
estimator of Quaini-Trojani-Yuan (2023) <doi:10.2139/ssrn.4574683> and the
factor screening procedure of Gospodinov-Kan-Robotti (2014)
<doi:10.2139/ssrn.2579821>. The functions for evaluating model
misspecification implement the HJ model misspecification distance of
Kan-Robotti (2008) <doi:10.1016/j.jempfin.2008.03.003>, which is a
modification of the prominent Hansen-Jagannathan (1997)
<doi:10.1111/j.1540-6261.1997.tb04813.x> distance. The functions for
testing model identification specialize the Kleibergen-Paap (2006)
<doi:10.1016/j.jeconom.2005.02.011> and the Chen-Fang (2019)
<doi:10.1111/j.1540-6261.1997.tb04813.x> rank test to the regression
coefficient matrix of test asset returns on risk factors. Finally, the
function for heteroskedasticity and autocorrelation robust covariance
estimation implements the Newey-West (1994) <doi:10.2307/2297912>
covariance estimator.

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
