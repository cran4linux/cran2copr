%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  AlphaPowerHazard
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Alpha-Power Hazard Regression Models for Survival Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-maxLik 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-maxLik 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-MASS 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-utils 

%description
Implements the alpha-power hazard model and regression frameworks for
survival data based on the flexible hazard rate function h(x; alpha, beta)
= alpha^x + x^(beta-1) (Pal et al., 2026
<doi:10.1007/s41096-026-00297-5>). Provides standard distribution
functions (d, p, q, r, h, H, s) and distributional properties including
raw/central moments, variance, skewness, kurtosis, quantile statistics
(Bowley's skewness, Moors's kurtosis), Lambert W hazard rate function
minimum (Corless et al., 1996), order statistics, and stochastic ordering
(Shaked & Shanthikumar, 1994). Computes five classical estimation methods
for baseline parameters: Maximum Likelihood Estimation (Casella & Berger,
2002), Least Squares Estimation (Swain et al., 1988), Weighted Least
Squares Estimation (Styan, 1973), Maximum Product of Spacings Estimation
(Cheng & Amin, 1983 <doi:10.1111/j.2517-6161.1983.tb01241.x>), and
Cramer-von Mises Estimation (Macdonald, 1971). Supports four hazard
regression models (M1-M4) within proportional hazards and parametric
frameworks across uncensored data, right censoring, left censoring,
interval censoring, and progressive Type-I and Type-II censoring schemes
(Lee & Wang, 2003; Lawless, 2011; Balakrishnan & Aggarwala, 2000).
Includes comprehensive model diagnostics, Cox-Snell, martingale, deviance,
standardized, and studentized residuals, leverage, Cook's distance,
DFFITS, DFBETAS, model comparisons (AIC, BIC, WAIC), k-fold
cross-validation, prediction suites, random data generators, and an
eight-panel diagnostic visualization suite.

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
