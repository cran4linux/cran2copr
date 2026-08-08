%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MultiFrailty
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Shared Frailty Regression Models with Inverse Gaussian, Generalized Lindley, and Gamma Frailty Distributions

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-maxLik 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-maxLik 
Requires:         R-CRAN-numDeriv 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-utils 

%description
Implements shared frailty regression models for survival data under eight
censoring mechanisms: exact, right censoring (Kalbfleisch and Prentice,
2002), left censoring, interval censoring (Sun, 2006), progressive Type I
censoring, and progressive Type II censoring (Balakrishnan and Aggarwala,
2000 <doi:10.1007/978-1-4612-1334-5>). Combines four frailty distributions
-- Gamma (Clayton, 1978), Inverse Gaussian (Hougaard, 1984), and two
variants of the Generalized Lindley (GL) distribution: GL Type 1, a
two-component gamma mixture with distribution-specific scale/shape linkage
(Pandey, Hanagal, and Tyagi, 2022), and GL Type 2, a two-component gamma
mixture with a common rate parameter (Pandey and Tyagi, 2021
<doi:10.1134/S1995080222010140>) -- with two baseline hazard
distributions: the two-parameter Weibull distribution (Weibull, 1951) and
the three-parameter Generalized (Exponentiated) Weibull distribution
(Mudholkar and Srivastava, 1993 <doi:10.1109/24.229504>). A no-frailty
baseline-only model is also supported for nested model comparison. Maximum
likelihood estimation is conducted using Newton-Raphson and
Broyden-Fletcher-Goldfarb-Shanno (BFGS) algorithms via the 'maxLik'
package (Henningsen and Toomet, 2011 <doi:10.1007/s00180-010-0217-1>).
Provides standard errors, confidence intervals, hypothesis tests, Akaike
Information Criterion (AIC, Akaike, 1974 <doi:10.1109/TAC.1974.1100705>),
Bayesian Information Criterion (BIC, Schwarz, 1978
<doi:10.1214/aos/1176344136>), corrected Akaike Information Criterion
(AICc, Hurvich and Tsai, 1989), Hannan-Quinn Information Criterion (HQIC,
Hannan and Quinn, 1979), a bootstrap approximation of the Widely
Applicable Information Criterion (WAIC, Watanabe, 2010), k-fold
cross-validation, frailty variance estimation, survival, hazard, median,
risk, and marginal predictions, Cox-Snell (Cox and Snell, 1968),
martingale (Barlow and Prentice, 1988), and deviance residuals with a
Kolmogorov-Smirnov goodness-of-fit test, influence diagnostics (leverage,
Cook's distance, difference in fits (DFFITS), difference in betas
(DFBETAS); Belsley, Kuh, and Welsch, 1980), random data generation under
all eight censoring mechanisms, a Monte Carlo simulation-study function,
and a diagnostic and survival plotting suite.

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
