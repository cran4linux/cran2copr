%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  projpred
%global packver   2.8.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.8.0
Release:          1%{?dist}%{?buildtag}
Summary:          Projection Predictive Feature Selection

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildRequires:    R-CRAN-rstantools >= 2.0.0
BuildRequires:    R-CRAN-loo >= 2.0.0
BuildRequires:    R-CRAN-lme4 >= 1.1.28
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-gamm4 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-ordinal 
BuildRequires:    R-CRAN-nnet 
BuildRequires:    R-CRAN-mclogit 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-rstantools >= 2.0.0
Requires:         R-CRAN-loo >= 2.0.0
Requires:         R-CRAN-lme4 >= 1.1.28
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-gamm4 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-ordinal 
Requires:         R-CRAN-nnet 
Requires:         R-CRAN-mclogit 

%description
Performs projection predictive feature selection for generalized linear
models (Piironen, Paasiniemi, and Vehtari, 2020, <doi:10.1214/20-EJS1711>)
with or without multilevel or additive terms (Catalina, Bürkner, and
Vehtari, 2022, <https://proceedings.mlr.press/v151/catalina22a.html>), for
some ordinal and nominal regression models (Weber, Glass, and Vehtari,
2023, <arXiv:2301.01660>), and for many other regression models (using the
latent projection by Catalina, Bürkner, and Vehtari, 2021,
<arXiv:2109.04702>, which can also be applied to most of the former
models). The package is compatible with the 'rstanarm' and 'brms'
packages, but other reference models can also be used. See the vignettes
and the documentation for more information and examples.

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
