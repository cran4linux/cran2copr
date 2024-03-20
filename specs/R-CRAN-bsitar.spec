%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bsitar
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Super Imposition by Translation and Rotation Growth Curve Analysis

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-loo >= 2.7.0
BuildRequires:    R-CRAN-Rdpack >= 2.5
BuildRequires:    R-CRAN-rstan >= 2.26.0
BuildRequires:    R-CRAN-brms >= 2.17.0
BuildRequires:    R-CRAN-dplyr >= 1.1.3
BuildRequires:    R-CRAN-rlang >= 1.1.2
BuildRequires:    R-CRAN-insight >= 0.19.7
BuildRequires:    R-CRAN-marginaleffects >= 0.18.0
BuildRequires:    R-CRAN-sitar 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-rstantools
Requires:         R-CRAN-loo >= 2.7.0
Requires:         R-CRAN-Rdpack >= 2.5
Requires:         R-CRAN-rstan >= 2.26.0
Requires:         R-CRAN-brms >= 2.17.0
Requires:         R-CRAN-dplyr >= 1.1.3
Requires:         R-CRAN-rlang >= 1.1.2
Requires:         R-CRAN-insight >= 0.19.7
Requires:         R-CRAN-marginaleffects >= 0.18.0
Requires:         R-CRAN-sitar 
Requires:         R-CRAN-magrittr 
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-CRAN-rstantools

%description
The Super Imposition by Translation and Rotation (SITAR) model is a
shape-invariant nonlinear mixed effect model that fits a natural cubic
spline mean curve to the growth data, and aligns individual-specific
growth curves to the underlying mean curve via a set of random effects
(see Cole, 2010 <doi:10.1093/ije/dyq115> for details). The non-Bayesian
version of the SITAR model can be fit by using an already available R
package 'sitar'. While 'sitar' package allows modelling of a single
outcome only, the 'bsitar' package offers a great flexibility in fitting
models of varying complexities that include joint modelling of multiple
outcomes such as height and weight (multivariate model). Also, the
'bsitar' package allows simultaneous analysis of a single outcome
separately for sub groups defined by a factor variable such as gender.
This is achieved by fitting separate models for each sub group (such as
males and females for gender variable). An advantage of such approach is
that posterior draws for each sub group are part of a single model object
that makes it possible to compare coefficients across groups and test
hypotheses. As 'bsitar' package is a front-end to the R package 'brms', it
offers an excellent support for post-processing of posterior draws via
various functions that are directly available from the 'brms' package. In
addition, the 'bsitar' package include various customized functions that
allow estimation and visualization growth curves such as distance
(increase in size with age) and velocity (change in growth rate as a
function of age).

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
