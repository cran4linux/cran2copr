%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  qbrms
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Quick Bayesian Regression Models Using 'INLA' with 'brms' Syntax

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-posterior 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-miniUI 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-CRAN-loo 
BuildRequires:    R-CRAN-TMB 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-methods 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-posterior 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-miniUI 
Requires:         R-CRAN-future 
Requires:         R-CRAN-future.apply 
Requires:         R-CRAN-loo 
Requires:         R-CRAN-TMB 
Requires:         R-CRAN-jsonlite 

%description
Provides a 'brms'-like interface for fitting Bayesian regression models
using 'INLA' (Integrated Nested Laplace Approximations) and 'TMB'
(Template Model Builder). The package offers faster model fitting while
maintaining familiar 'brms' syntax and output formats. Supports fixed and
mixed effects models, multiple probability distributions, conditional
effects plots, and posterior predictive checks with summary methods
compatible with 'brms'. 'TMB' integration provides fast ordinal regression
capabilities. Implements methods adapted from 'emmeans' for marginal means
estimation and 'bayestestR' for Bayesian inference assessment. Methods are
based on Rue et al. (2009) <doi:10.1111/j.1467-9868.2008.00700.x>,
Kristensen et al. (2016) <doi:10.18637/jss.v070.i05>, Lenth (2016)
<doi:10.18637/jss.v069.i01>, Bürkner (2017) <doi:10.18637/jss.v080.i01>,
Makowski et al. (2019) <doi:10.21105/joss.01541>, and Kruschke (2014,
ISBN:9780124058880).

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
