%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  nbsurv
%global packver   0.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.1
Release:          1%{?dist}%{?buildtag}
Summary:          Conditional Naive Bayes Survival Modelling for Right-Censored Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-graphics 
Requires:         R-CRAN-survival 
Requires:         R-stats 
Requires:         R-utils 

%description
Fits conditional naive Bayes survival models for right-censored outcomes
using inverse-probability of censoring weighting. The package provides
model fitting, prediction, resampling-based evaluation, cross-validation,
hyper-parameter tuning, and permutation variable importance utilities for
horizon-specific survival prediction. The model is the censored naive
Bayes classifier of Wolfson et al. (2015) <doi:10.1002/sim.6526>, which
combines the marginal Kaplan-Meier survivor function with horizon-specific
class-conditional covariate densities and inverse-probability-of-censoring
weights. Resampling evaluation uses the
inverse-probability-of-censoring-weighted Brier score of Gerds and
Schumacher (2006) <doi:10.1002/bimj.200610301>.

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
