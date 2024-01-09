%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mlrv
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Long-Run Variance Estimation in Time Series Regression

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-mathjaxr 
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-stats 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-RcppArmadillo 
Requires:         R-CRAN-mathjaxr 
Requires:         R-CRAN-xtable 
Requires:         R-stats 

%description
Plug-in and difference-based long-run covariance matrix estimation for
time series regression. Two applications of hypothesis testing are also
provided. The first one is for testing for structural stability in
coefficient functions. The second one is aimed at detecting long memory in
time series regression.

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
