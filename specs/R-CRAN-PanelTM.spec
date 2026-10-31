%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PanelTM
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Two- And Three-Way Dynamic Panel Threshold Regression Model for Change Point Detection

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-MASS 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-MASS 

%description
Estimation of two-way and three-way dynamic panel threshold regression
models using the first-differenced instrumental-variable generalized
method of moments (FD-IV-GMM) estimator. The implementation builds on Seo
and Shin (2016) <doi:10.1016/j.jeconom.2016.03.005> and Di Lascio and
Perazzini (2026) <doi:10.1007/s10260-026-00842-3>. The models accommodate
time-varying exogenous and endogenous regressors and allow the lagged
dependent variable to serve as the threshold variable. The package
includes a bootstrap-based test for threshold effects, a procedure for
identifying change points in individual time series, functions for
simulating two-way and three-way panel data with regime changes, and tools
for evaluating estimator performance through bias and root mean squared
error measures.

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
