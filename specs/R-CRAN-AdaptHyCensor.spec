%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  AdaptHyCensor
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Generalized Inference and Data Generation for Adaptive Progressive Hybrid Censoring Schemes

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-stats 
Requires:         R-graphics 

%description
Comprehensive computational tools for data generation, statistical
inference, and visual diagnostics under Adaptive Type-I and Adaptive
Type-II Progressive Hybrid Censoring Schemes. Users can supply custom
probability density functions (PDF), cumulative distribution functions
(CDF), survival functions, parameter ranges, and progressive schemes for
any univariate lifetime distribution. Parameter estimation methods include
Maximum Likelihood Estimation (MLE) using multiple optimization algorithms
(Newton-Raphson (NR), Broyden-Fletcher-Goldfarb-Shanno (BFGS), BFGS in R
(BFGSR), Berndt-Hall-Hall-Hausman (BHHH), Simulated Annealing (SANN),
Conjugate Gradients (CG), and Nelder-Mead (NM)), Bayesian estimation via
Gibbs and Metropolis-Hastings (M-H) MCMC sampling, Importance Sampling
(IS), and Lindley's approximation. Diagnostic tools provide histograms,
dot plots, and autocorrelation function (ACF) plots for model validation.
Methods are based on Balakrishnan, Cramer, and Kundu (2023,
ISBN:978-0-12-398387-9), Ng, Kundu, and Chan (2009, IEEE Transactions on
Reliability, 58, 634-642), Lin and Huang (2012, Journal of Statistical
Computation and Simulation, 82, 1005-1018), Lindley (1980, Journal of the
Royal Statistical Society, Series B, 42, 223-237), and Berndt, Hall, Hall,
and Hausman (1974, Annals of Economic and Social Measurement, 3, 653-665).

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
