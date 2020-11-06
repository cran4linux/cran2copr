%global packname  FlexReg
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Regression Models for Bounded Responses

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-rstan >= 2.18.1
BuildRequires:    R-CRAN-StanHeaders >= 2.18.0
BuildRequires:    R-CRAN-rstantools >= 2.0.0
BuildRequires:    R-CRAN-BH >= 1.66.0
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.3.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-loo 
BuildRequires:    R-CRAN-bayesplot 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-utils 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-rstantools
Requires:         R-CRAN-rstan >= 2.18.1
Requires:         R-CRAN-rstantools >= 2.0.0
Requires:         R-CRAN-Rcpp >= 0.12.0
Requires:         R-methods 
Requires:         R-CRAN-loo 
Requires:         R-CRAN-bayesplot 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-Formula 
Requires:         R-utils 
Requires:         R-grDevices 
Requires:         R-CRAN-rstantools

%description
Functions to fit regression models for bounded responses, such as rates
and proportions. Available models are the flexible beta (Migliorati, S.,
Di Brisco, A. M., Ongaro, A. (2018) <doi:10.1214/17-BA1079>), the
variance-inflated beta (Di Brisco, A. M., Migliorati, S., Ongaro, A.
(2020) <doi:10.1177/1471082X18821213>), and the beta one (Ferrari, S.L.P.,
and Cribari-Neto, F. (2004) <doi:10.1080/0266476042000214501>). Inference
is dealt with a Bayesian approach based on the Hamiltonian Monte Carlo
(HMC) algorithm (Gelman, A.; Carlin, J. B.; Stern, H. S. and Rubin, D. B.
(2014) <doi:10.1201/b16018>). Besides, functions to compute residuals,
posterior predictives, goodness-of-fit measures, convergence diagnostics,
and graphical representations are provided.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
