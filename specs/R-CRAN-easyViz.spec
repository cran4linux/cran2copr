%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  easyViz
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Easy Visualization of Conditional Effects from Regression Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-grDevices 

%description
Offers a flexible and user-friendly interface for visualizing conditional
effects from a broad range of regression models, including mixed-effects
and generalized additive (mixed) models. Compatible model types include
lm(), rlm(), glm(), glm.nb(), betareg(), and gam() (from 'mgcv');
nonlinear models via nls(); generalized least squares via gls(); and
survival models via coxph() (from 'survival'). Mixed-effects models with
random intercepts and/or slopes can be fitted using lmer(), glmer(),
glmer.nb(), glmmTMB(), or gam() (from 'mgcv', via smooth terms). Plots are
rendered using base R graphics with extensive customization options.
Approximate confidence intervals for nls() and betareg() models are
computed using the delta method. Robust standard errors for rlm() are
computed using the sandwich estimator (Zeileis 2004)
<doi:10.18637/jss.v011.i10>. For beta regression using 'betareg', see
Cribari-Neto and Zeileis (2010) <doi:10.18637/jss.v034.i02>. For
mixed-effects models with 'lme4', see Bates et al. (2015)
<doi:10.18637/jss.v067.i01>. For models using 'glmmTMB', see Brooks et al.
(2017) <doi:10.32614/RJ-2017-066>. Methods for generalized additive models
using 'mgcv' follow Wood (2017) <doi:10.1201/9781315370279>.

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
