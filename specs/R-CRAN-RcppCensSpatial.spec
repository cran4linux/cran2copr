%global __brp_check_rpaths %{nil}
%global packname  RcppCensSpatial
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Spatial Estimation and Prediction for Censored/Missing Responses

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-MomTrunc 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-relliptical 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-StempCens 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-RcppProgress 
BuildRequires:    R-CRAN-roptim 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-MomTrunc 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-relliptical 
Requires:         R-stats 
Requires:         R-CRAN-StempCens 

%description
It provides functions to estimate parameters in linear spatial models with
censored/missing responses via the Expectation-Maximization (EM), the
Stochastic Approximation EM (SAEM), or the Monte Carlo EM (MCEM)
algorithm. These algorithms are widely used to compute the maximum
likelihood (ML) estimates in problems with incomplete data. The EM
algorithm computes the ML estimates when a closed expression for the
conditional expectation of the complete-data log-likelihood function is
available. In the MCEM algorithm, the conditional expectation is
substituted by a Monte Carlo approximation based on many independent
simulations of the missing data. In contrast, the SAEM algorithm splits
the E-step into simulation and integration steps. This package also
approximates the standard error of the estimates using the Louis method.
Moreover, it has a function that performs spatial prediction in new
locations.

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
