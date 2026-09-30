%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  clis
%global packver   0.3.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.6
Release:          1%{?dist}%{?buildtag}
Summary:          Conformal Local Influence Screening for Bounded-Response Regression

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-gamlss.dist >= 6.0.0
BuildRequires:    R-CRAN-gamlss >= 5.4.0
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
Requires:         R-CRAN-gamlss.dist >= 6.0.0
Requires:         R-CRAN-gamlss >= 5.4.0
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-utils 

%description
Provides fast, statistically calibrated influence diagnostics for
zero-or-one inflated beta (BIc) regression models with variable
dispersion. The core idea is to use the conformal normal curvature of Poon
and Poon (1999) <doi:10.1111/1467-9868.00162> as a non-conformity score
within a split-conformal testing procedure, yielding per-observation
conformal p-values whose Benjamini-Hochberg adjustment controls the false
discovery rate at a user-specified level (Bates and others, 2023)
<doi:10.1214/22-AOS2244>. Unlike classical local influence diagnostics,
which rely on visual inspection of index plots and do not scale beyond a
few hundred observations, 'clis' provides a finite-sample error guarantee
and runs in linear time per observation after a single model fit. Methods
for four perturbation schemes, block decomposition of influence into the
inflation-probability and conditional-mean/precision components, penalised
additive (semiparametric) submodels, and a full suite of diagnostic plots
are included.

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
