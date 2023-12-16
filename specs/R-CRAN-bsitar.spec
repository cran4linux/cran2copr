%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bsitar
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Super Imposition by Translation and Rotation Growth Curve Analysis

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-Rdpack >= 2.5
BuildRequires:    R-CRAN-rstan >= 2.26.0
BuildRequires:    R-CRAN-brms >= 2.17.0
BuildRequires:    R-CRAN-dplyr >= 1.1.3
BuildRequires:    R-CRAN-rlang >= 1.1.2
BuildRequires:    R-CRAN-sitar 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-loo 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-rstantools
Requires:         R-CRAN-Rdpack >= 2.5
Requires:         R-CRAN-rstan >= 2.26.0
Requires:         R-CRAN-brms >= 2.17.0
Requires:         R-CRAN-dplyr >= 1.1.3
Requires:         R-CRAN-rlang >= 1.1.2
Requires:         R-CRAN-sitar 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-loo 
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-CRAN-rstantools

%description
The Super Imposition by Translation and Rotation (SITAR) model is a
shape-invariant nonlinear mixed effect model that fits a natural cubic
spline mean curve and and then aligns individual-specific growth curves to
the mean curve via a set of random effects on both effects. For more
details, please see Cole (2010) <doi:10.1093/ije/dyq115>. The non Bayesian
version of the SITAR model can be fit by using an already available R
package 'sitar'. However, the 'sitar' package allows modelling of a single
outcome only. The 'bsitar' package, in addition to fitting SITAR to a
single outcome, offers a great flexibility in fitting models of varying
complexities that include joint modelling of multiple outcomes
(multivariate model) such as height and weight, and to fit separate models
defined by sub group such as gender when analyzing a single outcome.
Furthermore, since the 'bsitar' package is a front-end to the R package
'brms', it offers an excellent support for post-processing of posterior
draws which is available from the 'brms' package.

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
