%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CausalSpline
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Nonlinear Causal Dose-Response Estimation via Splines

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-splines 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-CRAN-boot 
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-splines 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-sandwich 
Requires:         R-CRAN-boot 

%description
Estimates nonlinear causal dose-response functions for continuous
treatments using spline-based methods under standard causal assumptions
(unconfoundedness / ignorability). Implements three identification
strategies: Inverse Probability Weighting (IPW) via the generalised
propensity score (GPS), G-computation (outcome regression), and a
doubly-robust combination. Natural cubic splines and B-splines are
supported for both the exposure-response curve f(T) and the propensity
nuisance model. Pointwise confidence bands are obtained via the sandwich
estimator or nonparametric bootstrap. Also provides fragility diagnostics
including pointwise curvature-based fragility, uncertainty-normalised
fragility, and regional integration over user-defined treatment intervals.
Builds on the framework of Hirano and Imbens (2004)
<doi:10.1111/j.1468-0262.2004.00481.x> for continuous treatments and
extends it to fully nonparametric spline estimation.

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
