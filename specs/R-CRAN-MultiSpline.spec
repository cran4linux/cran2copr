%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MultiSpline
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Spline-Based Nonlinear Modeling for Multilevel and Longitudinal Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-rlang 

%description
Provides tools for fitting, predicting, and visualizing nonlinear
relationships in single-level, multilevel, and longitudinal regression
models. Nonlinear functional forms are represented using natural cubic
splines from 'splines' and smooth terms from 'mgcv'. The package offers a
unified interface for specifying nonlinear effects, interactions with time
variables, random-intercept clustering structures, and additional linear
covariates. Utilities are included to generate prediction grids and
produce effect plots, facilitating interpretation and visualization of
nonlinear relationships in applied regression workflows. The
implementation builds on established methods for spline-based regression
and mixed-effects modeling (Hastie and Tibshirani, 1990
<doi:10.1201/9780203738535>; Bates et al., 2015
<doi:10.18637/jss.v067.i01>; Wood, 2017 <doi:10.1201/9781315370279>).
Applications include hierarchical and longitudinal data structures common
in education, health, and social science research.

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
