%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  spboost
%global packver   0.7.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.0
Release:          1%{?dist}%{?buildtag}
Summary:          Gradient Boosting for Nonlinear Spatial Autoregressive Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-mboost 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-mgwrsar 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-xgboost 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-nabor 
BuildRequires:    R-CRAN-earth 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-mboost 
Requires:         R-CRAN-mgcv 
Requires:         R-methods 
Requires:         R-CRAN-mgwrsar 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-xgboost 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-nabor 
Requires:         R-CRAN-earth 

%description
Flexible nonlinear extension of spatial autoregressive (SAR), spatial
error (SEM), and spatial autoregressive with autoregressive disturbances
(SARAR) models with multiple regression engines (generalized additive
models ('mgcv'), gradient boosting ('mboost'), multivariate adaptive
regression splines ('earth'), and 'xgboost') and two families of
spatial-parameter estimators: maximum likelihood and the determinant-free
Closed-Form Estimator of Smirnov (2020) <doi:10.1111/gean.12268>. See
Geniaux G. (2026). "Flexible nonlinear spatial autoregressive models: a
gradient boosting approach with closed-form estimation." Presented at
Spatial Econometrics World Congress (SEA/SEW 2026, Paris), unpublished.

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
