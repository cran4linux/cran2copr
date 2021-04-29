%global packname  audrex
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Automatic Dynamic Regression using Extreme Gradient Boosting

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-rBayesianOptimization 
BuildRequires:    R-CRAN-xgboost 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-narray 
BuildRequires:    R-CRAN-fANCOVA 
BuildRequires:    R-CRAN-imputeTS 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-tictoc 
BuildRequires:    R-CRAN-bizdays 
Requires:         R-CRAN-rBayesianOptimization 
Requires:         R-CRAN-xgboost 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-narray 
Requires:         R-CRAN-fANCOVA 
Requires:         R-CRAN-imputeTS 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-tictoc 
Requires:         R-CRAN-bizdays 

%description
Dynamic regression for time series using Extreme Gradient Boosting with
hyper-parameter tuning via Bayesian Optimization.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
