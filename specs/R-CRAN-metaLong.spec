%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  metaLong
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Longitudinal Meta-Analysis with Robust Variance Estimation and Sensitivity Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-metafor >= 3.8.1
BuildRequires:    R-splines 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-metafor >= 3.8.1
Requires:         R-splines 
Requires:         R-stats 
Requires:         R-utils 

%description
Tools for longitudinal meta-analysis where studies contribute effect sizes
at multiple follow-up time points. Implements robust variance estimation
(RVE) with Tipton small-sample corrections following Hedges, Tipton, and
Johnson (2010) <doi:10.1002/jrsm.5> and Tipton (2015)
<doi:10.1037/met0000011>, time-varying sensitivity analysis via the Impact
Threshold for a Confounding Variable (ITCV) following Frank (2000)
<doi:10.1177/0049124100029002003>, benchmark calibration of the ITCV
threshold against observed study-level covariates, spline-based nonlinear
time-trend modeling with a nonlinearity test, and leave-k-out fragility
analysis across the follow-up trajectory. Designed for researchers
synthesising evidence from studies with repeated outcome measurement in
education, psychology, health, and the social sciences.

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
