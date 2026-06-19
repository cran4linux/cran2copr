%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  GammaFrailty
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Gamma Frailty Regression Models with Multiple Baseline Distributions

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
Implements univariate gamma frailty regression models for survival data
with six different baseline distributions: the Arvind distribution (Pandey
et al., 2024), the Lindley distribution (Lindley, 1958), the Linear
Failure Rate distribution (Bain, 1974), the Power Xgamma distribution
(Tyagi et al., 2022), the Modified Topp-Leone distribution (Singh et al.,
2025), and the Power Failure Rate distribution (Mugdadi, 2005). The
package supports uncensored (complete) and censored data (right, left,
interval, and progressive censoring) with and without covariates. It
provides maximum likelihood estimation, standard errors, confidence
intervals, t-statistics, p-values, Akaike Information Criterion (AIC),
Bayesian Information Criterion (BIC), a bootstrap approximation of the
Widely Applicable Information Criterion (WAIC), k-fold cross-validation,
variance inflation factors, R-squared, adjusted R-squared, Mean Squared
Error (MSE), Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), an
overall model F-test, frailty variance estimation, survival probabilities
at user-specified time points, median survival, expected survival within a
fixed window, risk predictions, marginal predictions, martingale and
deviance residuals, standardized and studentized residuals, leverage
values, Cook's distance, Difference in Fits (DFFITS), Difference in Betas
(DFBETAS), and a comprehensive suite of diagnostic and survival plots
including Kaplan-Meier overlays and coefficient forest plots. Random
number generation is available for each baseline distribution and the full
frailty model, and a simulation study function evaluates parameter
recovery across sample sizes and censoring scenarios. References are
Lindley (1958) <doi:10.1111/j.2517-6161.1958.tb00278.x>, Mugdadi (2005)
<doi:10.1016/j.amc.2004.09.064>, Bain (1974)
<doi:10.1080/00401706.1974.10489237>, Singh, Tyagi, Singh, and Tyagi
(2025)
<https://ph02.tci-thaijo.org/index.php/thaistat/article/view/257215>,
Pandey, Singh, Tyagi, and Tyagi (2024) <https://ssca.org.in/journal.html>,
and Tyagi, Kumar, Pandey, Saha, and Bagariya (2022) <https://ijsreg.com/>.

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
