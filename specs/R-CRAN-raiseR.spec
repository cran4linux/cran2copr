%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  raiseR
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Raise Regression and Robust Methods for Multicollinearity

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-mrfDepth 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-withr 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-mrfDepth 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-withr 

%description
Implements Raise Regression as an inference-preserving alternative to
Ridge Regression for combating multicollinearity in linear models,
including the classical single-variable Raise Regression, the Simultaneous
Raise Regression (SRR) based on QR decomposition and the Sequential
Variance Inflation Factor (SVIF) of Jacob and Varadharajan (2022)
<doi:10.1007/s11135-022-01557-9>, and the original raise parameter
selection strategy of Jacob and Varadharajan (2023)
<doi:10.13189/ms.2023.110106>. Also implements Robust Raise Regression for
data contaminated by outliers, with exact finite-sample inference
(sandwich standard errors, Wald tests, Satterthwaite-corrected degrees of
freedom) obtained by down-weighting observations using Stahel-Donoho
projection outlyingness and Tukey's biweight function. Provides ordinary
and robust Ridge Regression (Hoerl and Kennard, 1970,
<doi:10.1080/00401706.1970.10488634>), ordinary and robust Liu Regression
(Liu, 1993, <doi:10.1080/03610929308831027>), with the robust variants of
both based on the MM-estimates of Yohai (1987,
<doi:10.1214/aos/1176350366>) and, for Liu Regression specifically, the
biasing-parameter derivation of Filzmoser and Kurnaz (2018)
<doi:10.1080/03610918.2016.1271889>. Also provides the classical Variance
Inflation Factor (VIF) and Condition Number (Belsley, 1991) computed from
the correlation matrix of the predictors, and the Robust Variance
Inflation Factor (RVIF) and robust Condition Number of Jacob and
Varadharajan (2024, Sankhya B, <doi:10.1007/s13571-024-00342-y>), which
use the same projection outlyingness and biweight down-weighting scheme to
obtain a weighted correlation matrix that resists the influence of
outliers. A flexible scaleDat() function supports classical (mean and
standard deviation), robust weighted (Stahel-Donoho and Tukey biweight),
median and Median Absolute Deviation Normalized (MADN, the median absolute
deviation scaled by 1.4826 to estimate the standard deviation under
normality), and min-max scaling. Diagnostic and goodness-of-fit plots, and
the standard influence-diagnostic suite (Cook's distance, DFBETAS and
COVRATIO regression diagnostics) and heteroskedasticity tests (via the
'lmtest' and 'car' packages) analogous to those for objects of class 'lm',
are provided for the exact, unbiased Raise Regression fit.

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
