%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  VCA
%global packver   1.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.0
Release:          1%{?dist}%{?buildtag}
Summary:          Variance Component Analysis

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-numDeriv 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-Matrix 
Requires:         R-methods 
Requires:         R-CRAN-numDeriv 

%description
ANOVA and REML estimation of linear mixed models is implemented, once
following Searle et al. (1991, ANOVA for unbalanced data), once making use
of the 'lme4' package. The primary objective of this package is to perform
a variance component analysis (VCA) according to CLSI EP05-A3 guideline
"Evaluation of Precision of Quantitative Measurement Procedures" (2014).
There are plotting methods for visualization of an experimental design,
plotting random effects and residuals. For ANOVA type estimation two
methods for computing ANOVA mean squares are implemented (SWEEP and
quadratic forms). The covariance matrix of variance components can be
derived, which is used in estimating confidence intervals. Linear
hypotheses of fixed effects and LS means can be computed. LS means can be
computed at specific values of covariables and with custom weighting
schemes for factor variables. See ?VCA for a more comprehensive
description of the features.

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
