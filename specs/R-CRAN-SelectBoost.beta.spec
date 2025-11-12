%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SelectBoost.beta
%global packver   0.4.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.5
Release:          1%{?dist}%{?buildtag}
Summary:          Stability-Selection via Correlated Resampling for Beta-Regression Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildRequires:    R-CRAN-betareg 
BuildRequires:    R-CRAN-gamlss 
BuildRequires:    R-CRAN-gamlss.dist 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-withr 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-betareg 
Requires:         R-CRAN-gamlss 
Requires:         R-CRAN-gamlss.dist 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-CRAN-withr 

%description
Adds variable-selection functions for Beta regression models (both mean
and phi submodels) so they can be used within the 'SelectBoost' algorithm.
Includes stepwise AIC, BIC, and corrected AIC on betareg() fits,
'gamlss'-based LASSO/Elastic-Net, a pure 'glmnet' iterative re-weighted
least squares-based selector with an optional standardization speedup, and
'C++' helpers for iterative re-weighted least squares working steps and
precision updates. Also provides a fastboost_interval() variant for
interval responses, comparison helpers, and a flexible simulator
simulation_DATA.beta() for interval-valued data. For more details see
Bertrand and Maumy (2023) <doi:10.7490/f1000research.1119552.1>.

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
