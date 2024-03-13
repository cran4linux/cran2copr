%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rmsb
%global packver   1.1-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Regression Modeling Strategies

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-rms >= 6.8.0
BuildRequires:    R-CRAN-RcppParallel >= 5.0.1
BuildRequires:    R-CRAN-Hmisc >= 4.3.0
BuildRequires:    R-CRAN-survival >= 3.1.12
BuildRequires:    R-CRAN-rstan >= 2.26.23
BuildRequires:    R-CRAN-StanHeaders >= 2.18.0
BuildRequires:    R-CRAN-BH >= 1.66.0
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.3.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-loo 
BuildRequires:    R-CRAN-rstantools
Requires:         R-CRAN-rms >= 6.8.0
Requires:         R-CRAN-Hmisc >= 4.3.0
Requires:         R-CRAN-survival >= 3.1.12
Requires:         R-CRAN-rstan >= 2.26.23
Requires:         R-CRAN-Rcpp >= 0.12.0
Requires:         R-methods 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-loo 
Requires:         R-CRAN-rstantools

%description
A Bayesian companion to the 'rms' package, 'rmsb' provides Bayesian model
fitting, post-fit estimation, and graphics.  It implements Bayesian
regression models whose fit objects can be processed by 'rms' functions
such as 'contrast()', 'summary()', 'Predict()', 'nomogram()', and
'latex()'.  The fitting function currently implemented in the package is
'blrm()' for Bayesian logistic binary and ordinal regression with optional
clustering, censoring, and departures from the proportional odds
assumption using the partial proportional odds model of Peterson and
Harrell (1990) <https://www.jstor.org/stable/2347760>.

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
