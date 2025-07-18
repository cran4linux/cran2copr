%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  parTimeROC
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Parametric Time-Dependent Receiver Operating Characteristic

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-RcppParallel >= 5.0.1
BuildRequires:    R-CRAN-survival >= 3.5.5
BuildRequires:    R-CRAN-VineCopula >= 2.4.5
BuildRequires:    R-CRAN-rstantools >= 2.4.0
BuildRequires:    R-CRAN-flexsurv >= 2.2.2
BuildRequires:    R-CRAN-rstan >= 2.18.1
BuildRequires:    R-CRAN-StanHeaders >= 2.18.0
BuildRequires:    R-CRAN-sn >= 2.1.1
BuildRequires:    R-CRAN-BH >= 1.66.0
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.3.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.0
BuildRequires:    R-CRAN-cubature 
BuildRequires:    R-CRAN-DescTools 
BuildRequires:    R-CRAN-GofCens 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-moments 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-rstantools
Requires:         R-CRAN-RcppParallel >= 5.0.1
Requires:         R-CRAN-survival >= 3.5.5
Requires:         R-CRAN-VineCopula >= 2.4.5
Requires:         R-CRAN-rstantools >= 2.4.0
Requires:         R-CRAN-flexsurv >= 2.2.2
Requires:         R-CRAN-rstan >= 2.18.1
Requires:         R-CRAN-sn >= 2.1.1
Requires:         R-CRAN-Rcpp >= 0.12.0
Requires:         R-CRAN-cubature 
Requires:         R-CRAN-DescTools 
Requires:         R-CRAN-GofCens 
Requires:         R-graphics 
Requires:         R-CRAN-Matrix 
Requires:         R-methods 
Requires:         R-CRAN-moments 
Requires:         R-CRAN-mvtnorm 
Requires:         R-stats 
Requires:         R-CRAN-rstantools

%description
Producing the time-dependent receiver operating characteristic (ROC) curve
through parametric approaches. Tools for generating random data, fitting,
predicting and check goodness of fit are prepared. The methods are
developed from the theoretical framework of proportional hazard model and
copula functions. Using this package, users can now simulate parametric
time-dependent ROC and run experiment to understand the behavior of the
curve under different scenario.

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
