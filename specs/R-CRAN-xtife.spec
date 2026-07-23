%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  xtife
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          1%{?dist}%{?buildtag}
Summary:          Interactive Fixed Effects Estimator for Panel Data

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats 
Requires:         R-stats 

%description
Implements the interactive fixed effects ('IFE') panel estimator of Bai
(2009) <doi:10.3982/ECTA6135> for balanced and unbalanced panels, with
optional additive unit and/or time fixed effects. Provides analytical
standard errors ('homoskedastic', 'HC1' heteroskedasticity-robust,
cluster-robust by unit, and heteroskedasticity- and autocorrelation-
consistent), together with asymptotic incidental-parameter bias correction
for large panels, including a dynamic extension for predetermined
(lagged-dependent) regressors following Moon and Weidner (2017)
<doi:10.1017/S0266466615000328>. The number of factors is chosen by
information criteria (Bai and Ng 2002 <doi:10.1111/1468-0262.00273>) or by
singular value thresholding. Unbalanced panels are handled by an
expectation-maximisation algorithm with nuclear-norm-regularised
initialisation, with estimation, analytical inference, and bias correction
following Su, Wang and Wang (2025) <doi:10.2139/ssrn.5177283> and building
on the matrix-completion and missing-data factor analysis of Bai and Ng
(2021) <doi:10.1080/01621459.2021.1967163>. All computations use base R
only, with no external dependencies.

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
