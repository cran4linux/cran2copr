%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ForceChoice
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Forced-Choice Modeling Based on Item Response Theory and Cognitive Diagnostic Models

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-RcppParallel >= 5.0.1
BuildRequires:    R-CRAN-rstantools >= 2.6.0
BuildRequires:    R-CRAN-rstan >= 2.18.1
BuildRequires:    R-CRAN-StanHeaders >= 2.18.0
BuildRequires:    R-CRAN-BH >= 1.66.0
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.3.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.0
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-GPArotation 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-rstantools
Requires:         R-CRAN-RcppParallel >= 5.0.1
Requires:         R-CRAN-rstantools >= 2.6.0
Requires:         R-CRAN-rstan >= 2.18.1
Requires:         R-CRAN-Rcpp >= 0.12.0
Requires:         R-CRAN-coda 
Requires:         R-CRAN-GPArotation 
Requires:         R-CRAN-MASS 
Requires:         R-methods 
Requires:         R-CRAN-numDeriv 
Requires:         R-parallel 
Requires:         R-CRAN-rstantools

%description
Fits, simulates, and evaluates forced-choice and traditional item response
theory (IRT) models for noncognitive assessment. Eight model families are
supported, spanning dominance (multidimensional IRT (MIRT) 1PL--4PL;
multidimensional generalized partial credit model (MGPCM)), ideal-point
unfolding (multidimensional generalized graded unfolding model (MGGUM)),
and forced-choice designs (forced-choice multidimensional IRT (FCMIRT),
forced-choice generalized graded unfolding model (FCGGUM), Thurstonian IRT
(TIRT), forced-choice diagnostic classification model (FCDCM),
forced-choice generalized deterministic inputs, noisy "and" gate model
(FCGDINA)) that mitigate response biases such as acquiescence and social
desirability. Core estimation backends include full Bayesian inference via
Hamiltonian Monte Carlo (Stan) and a fast improved stochastic
expectation-maximization (iStEM) algorithm suitable for large-scale data;
FCGDINA also provides a deterministic expectation-maximization (EM)
estimator. Comprehensive model evaluation uses the limited-information M2
family of goodness-of-fit statistics (Maydeu-Olivares and Joe, 2005
<doi:10.1198/016214504000002069>; 2006 <doi:10.1007/s11336-005-1295-9>)
together with root mean square error of approximation (RMSEA), comparative
fit index (CFI), Tucker-Lewis index (TLI), and standardized root mean
square residual (SRMSR).

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
