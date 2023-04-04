%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  glmmPen
%global packver   1.5.3.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.3.4
Release:          1%{?dist}%{?buildtag}
Summary:          High Dimensional Penalized Generalized Linear Mixed Models (pGLMM)

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildRequires:    R-CRAN-rstan >= 2.18.1
BuildRequires:    R-CRAN-StanHeaders >= 2.18.0
BuildRequires:    R-CRAN-BH >= 1.66.0
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.3.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.0
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-bigmemory 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-ncvreg 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-coxme 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-rstantools 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-RcppParallel 
BuildRequires:    R-CRAN-rstantools
Requires:         R-CRAN-rstan >= 2.18.1
Requires:         R-CRAN-Rcpp >= 0.12.0
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-bigmemory 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-Matrix 
Requires:         R-methods 
Requires:         R-CRAN-ncvreg 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-coxme 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-rstantools 
Requires:         R-CRAN-rstantools

%description
Fits high dimensional penalized generalized linear mixed models using the
Monte Carlo Expectation Conditional Minimization (MCECM) algorithm. The
purpose of the package is to perform variable selection on both the fixed
and random effects simultaneously for generalized linear mixed models. The
package supports fitting of Binomial, Gaussian, and Poisson data with
canonical links, and supports penalization using the MCP, SCAD, or LASSO
penalties. The MCECM algorithm is described in Rashid et al. (2020)
<doi:10.1080/01621459.2019.1671197>. The techniques used in the
minimization portion of the procedure (the M-step) are derived from the
procedures of the 'ncvreg' package (Breheny and Huang (2011)
<doi:10.1214/10-AOAS388>) and 'grpreg' package (Breheny and Huang (2015)
<doi:10.1007/s11222-013-9424-2>), with appropriate modifications to
account for the estimation and penalization of the random effects. The
'ncvreg' and 'grpreg' packages also describe the MCP, SCAD, and LASSO
penalties.

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
