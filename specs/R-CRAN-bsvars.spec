%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bsvars
%global packver   3.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Estimation of Structural Vector Autoregressive Models

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.7
BuildRequires:    R-CRAN-RcppProgress >= 0.1
BuildRequires:    R-CRAN-RcppTN 
BuildRequires:    R-CRAN-GIGrvg 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-stochvol 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 1.0.7
Requires:         R-CRAN-RcppProgress >= 0.1
Requires:         R-CRAN-RcppTN 
Requires:         R-CRAN-GIGrvg 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-stochvol 

%description
Provides fast and efficient procedures for Bayesian analysis of Structural
Vector Autoregressions. This package estimates a wide range of models,
including homo-, heteroskedastic, and non-normal specifications.
Structural models can be identified by adjustable exclusion restrictions,
time-varying volatility, or non-normality. They all include a flexible
three-level equation-specific local-global hierarchical prior distribution
for the estimated level of shrinkage for autoregressive and structural
parameters. Additionally, the package facilitates predictive and
structural analyses such as impulse responses, forecast error variance and
historical decompositions, forecasting, verification of
heteroskedasticity, non-normality, and hypotheses on autoregressive
parameters, as well as analyses of structural shocks, volatilities, and
fitted values. Beautiful plots, informative summary functions, and
extensive documentation complement all this. The implemented techniques
align closely with those presented in Lütkepohl, Shang, Uzeda, & Woźniak
(2024) <doi:10.48550/arXiv.2404.11057>, Lütkepohl & Woźniak (2020)
<doi:10.1016/j.jedc.2020.103862>, and Song & Woźniak (2021)
<doi:10.1093/acrefore/9780190625979.013.174>.

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
