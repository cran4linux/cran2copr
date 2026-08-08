%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ImpAdaptType2Censor
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Data Generation and Statistical Inference for Improved Adaptive Type-II Progressive Censoring Schemes

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 

%description
Comprehensive computational routines for random data generation, Maximum
Likelihood Estimation (MLE), Maximum Product of Spacings Estimation
(MPSE), and MCMC Bayesian estimation under the Improved Adaptive Type-II
Progressive Censoring Scheme (IAT-II PCS). Users can supply custom
probability density functions (PDF), cumulative distribution functions
(CDF), survival functions, parameter ranges, and progressive censoring
plans for any continuous univariate lifetime distribution, or rely on
built-in parametric models (e.g., Generalized Exponential). Point
estimation methods include MLE via optimization algorithms
(Broyden-Fletcher-Goldfarb-Shanno (BFGS), Newton-Raphson (NR), Nelder-Mead
(NM), Conjugate Gradients (CG), L-BFGS-B, Simulated Annealing (SANN), and
Berndt-Hall-Hall-Hausman (BHHH)) and MPSE. Bayesian inference utilizes
Metropolis-Hastings within Gibbs sampling under Squared Error Loss (SEL)
and LINEX Loss (LL) functions to compute point estimates and Highest
Posterior Density (HPD) credible intervals. Asymptotic confidence
intervals for parameters, reliability, and hazard rate functions are
constructed using asymptotic normality and delta method. Methods are based
on Dev and Chacko (2026, Journal of the Iranian Statistical Society, 25,
1-29), Yan, Zhang, and Dong (2021, Journal of Computational and Applied
Mathematics, 381, 113022, <doi:10.1016/j.cam.2020.113022>), Ng, Kundu, and
Chan (2004, Naval Research Logistics, 51, 1145-1168,
<doi:10.1002/nav.20045>), Cheng and Amin (1983, Journal of the Royal
Statistical Society Series B, 45, 394-403,
<doi:10.1111/j.2517-6161.1983.tb01268.x>), Kundu and Gupta (1999,
Australian & New Zealand Journal of Statistics, 41, 173-188,
<doi:10.1111/1467-842X.00072>), and Berndt, Hall, Hall, and Hausman (1974,
Annals of Economic and Social Measurement, 3, 653-665).

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
