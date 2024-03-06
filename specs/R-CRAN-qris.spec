%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  qris
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Quantile Regression Model for Residual Lifetime Using an Induced Smoothing Approach

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildRequires:    R-CRAN-nleqslv 
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-nleqslv 
Requires:         R-CRAN-quantreg 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-Rcpp 

%description
A collection of functions is provided by this package to fit quantiles
regression models for censored residual lifetimes. It provides various
options for regression parameters estimation: the induced smoothing
approach (smooth), and L1-minimization (non-smooth).  It also implements
the estimation methods for standard errors of the regression parameters
estimates based on an efficient partial multiplier bootstrap method and
robust sandwich estimator. Furthermore, a simultaneous procedure of
estimating regression parameters and their standard errors via an
iterative updating procedure is implemented (iterative). For more details,
see Kim, K. H., Caplan, D. J., & Kang, S. (2022), "Smoothed quantile
regression for censored residual life", Computational Statistics, 1-22
<doi:10.1007/s00180-022-01262-z>.

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
