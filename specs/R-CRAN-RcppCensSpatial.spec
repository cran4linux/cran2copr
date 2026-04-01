%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RcppCensSpatial
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
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
It provides functions for estimating parameters in linear spatial models
with censored or missing responses using the Expectation-Maximization
(EM), Stochastic Approximation EM (SAEM), and Monte Carlo EM (MCEM)
algorithms. These methods are widely used to obtain maximum likelihood
(ML) estimates in the presence of incomplete data. The EM algorithm
computes ML estimates when a closed-form expression for the conditional
expectation of the complete-data log-likelihood is available. The MCEM
algorithm replaces this expectation with a Monte Carlo approximation based
on independent simulations of the missing data. In contrast, the SAEM
algorithm decomposes the E-step into simulation and stochastic
approximation steps, improving computational efficiency in complex
settings. In addition, the package provides standard error estimation
based on the Louis method. It also includes functionality for spatial
prediction at new locations. References used for this package: Galarza, C.
E., Matos, L. A., Castro, L. M., & Lachos, V. H. (2022). Moments of the
doubly truncated selection elliptical distributions with emphasis on the
unified multivariate skew-t distribution. Journal of Multivariate
Analysis, 189, 104944 <doi:10.1016/j.jmva.2021.104944>; Valeriano, K. A.,
Galarza, C. E., & Matos, L. A. (2023). Moments and random number
generation for the truncated elliptical family of distributions.
Statistics and Computing, 33(1), 32 <doi:10.1007/s11222-022-10200-4>.

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
