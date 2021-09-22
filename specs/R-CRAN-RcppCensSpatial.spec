%global __brp_check_rpaths %{nil}
%global packname  RcppCensSpatial
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Spatial Estimation and Prediction for Censored/Missing Responses

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-MomTrunc 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tlrmvnmvt 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-RcppProgress 
BuildRequires:    R-CRAN-roptim 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-MomTrunc 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-Rdpack 
Requires:         R-stats 
Requires:         R-CRAN-tlrmvnmvt 

%description
It provides functions to estimate the parameters in spatial models with
censored/missing responses via the Expectation-Maximization (EM) algorithm
(see Dempster, Laird, and Rubin
(1977)<https://www.jstor.org/stable/2984875>), the Stochastic
Approximation EM (SAEM) algorithm (see Delyon, Lavielle, and Moulines
(1999)<https://www.jstor.org/stable/120120>), and the Monte Carlo EM
(MCEM) algorithm (see Wei and Tanner
(1990)<doi:10.1080/01621459.1990.10474930>). These algorithms are widely
used to compute the maximum likelihood (ML) estimates in incomplete data
problems. The EM algorithm computes the ML estimates when a closed
expression for the conditional expectation of the complete-data
log-likelihood function is available. In the MCEM algorithm, the
conditional expectation is substituted by a Monte Carlo approximation
based on many independent simulations of the missing data, while the SAEM
algorithm splits the E-step into a simulation step and an integration
step. The SAEM algorithm was developed as an alternative to the
computationally intensive MCEM algorithm. This package also approximates
the standard error of the estimates using the method developed by Louis
(1982)<https://www.jstor.org/stable/2345828>. It also has a function that
performs spatial prediction in a set of new locations. Besides the
functions to estimate parameters, this package allows computing the
covariance matrix and the distance matrix.

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
