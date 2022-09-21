%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  projpred
%global packver   2.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Projection Predictive Feature Selection

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-loo >= 2.0.0
BuildRequires:    R-CRAN-rstantools >= 2.0.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-gamm4 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-loo >= 2.0.0
Requires:         R-CRAN-rstantools >= 2.0.0
Requires:         R-methods 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-Rcpp 
Requires:         R-utils 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-gamm4 
Requires:         R-CRAN-rlang 

%description
Performs projection predictive feature selection for generalized linear
and additive models as well as for generalized linear and additive
multilevel models (see Piironen, Paasiniemi and Vehtari, 2020,
<doi:10.1214/20-EJS1711>; Catalina, Bürkner and Vehtari, 2020,
<arXiv:2010.06994>). The package is compatible with the 'rstanarm' and
'brms' packages, but other reference models can also be used. See the
documentation as well as the package vignette for more information and
examples.

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
