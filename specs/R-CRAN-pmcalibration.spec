%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pmcalibration
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Calibration Curves for Clinical Prediction Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-splines 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-parallel 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-mgcv 
Requires:         R-splines 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-pbapply 
Requires:         R-parallel 
Requires:         R-grDevices 

%description
Fit calibrations curves for clinical prediction models and calculate
several associated metrics (Eavg, E50, E90, Emax). Ideally predicted
probabilities from a prediction model should align with observed
probabilities. Calibration curves relate predicted probabilities (or a
transformation thereof) to observed outcomes via a flexible non-linear
smoothing function. 'pmcalibration' allows users to choose between several
smoothers (regression splines, generalized additive models/GAMs, lowess,
loess). Both binary and time-to-event outcomes are supported. See Van
Calster et al. (2016) <doi:10.1016/j.jclinepi.2015.12.005>; Austin and
Steyerberg (2019) <doi:10.1002/sim.8281>; Austin et al. (2020)
<doi:10.1002/sim.8570>.

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
