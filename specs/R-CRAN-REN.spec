%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  REN
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Regularization Ensemble for Robust Portfolio Optimization

License:          AGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-tictoc 
BuildRequires:    R-CRAN-corpcor 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-stats 
BuildRequires:    R-parallel 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-quadprog 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-tictoc 
Requires:         R-CRAN-corpcor 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-foreach 
Requires:         R-stats 
Requires:         R-parallel 

%description
Portfolio optimization is achieved through a combination of regularization
techniques and ensemble methods that are designed to generate stable
out-of-sample return predictions, particularly in the presence of strong
correlations among assets. The package includes functions for data
preparation, parallel processing, and portfolio analysis using methods
such as Mean-Variance, James-Stein, LASSO, Ridge Regression, and Equal
Weighting. It also provides visualization tools and performance metrics,
such as the Sharpe ratio, volatility, and maximum drawdown, to assess the
results.

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
