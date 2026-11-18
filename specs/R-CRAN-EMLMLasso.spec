%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  EMLMLasso
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          EM Algorithm for Lasso-Penalized Linear Mixed Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-glmnet 
Requires:         R-graphics 
Requires:         R-CRAN-mvtnorm 
Requires:         R-stats 
Requires:         R-utils 

%description
Fits linear mixed models with a lasso penalty on the fixed-effects
coefficients via an Expectation-Maximization (EM) algorithm. Random
effects are treated as missing data at each E-step and the fixed-effects
update is solved with a coordinate-descent lasso ('glmnet'), so the same
penalized-likelihood machinery used for ordinary linear models extends
naturally to clustered/longitudinal data. By default, EMLMLasso() fits the
model over a data-driven grid of penalty values and selects the tuning
parameter by Bayesian Information Criterion. This is a modification of the
method of Oliveira, Schumacher, and Lachos (2026)
<doi:10.1177/09622802251399913>, in which the tuning parameter is
re-selected by cross-validation at every EM iteration.

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
