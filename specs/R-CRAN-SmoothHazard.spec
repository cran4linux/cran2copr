%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SmoothHazard
%global packver   2024.04.10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2024.04.10
Release:          1%{?dist}%{?buildtag}
Summary:          Estimation of Smooth Hazard Models for Interval-Censored Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 1.9.1
Requires:         R-core >= 1.9.1
BuildRequires:    R-CRAN-prodlim >= 1.4.9
BuildRequires:    R-CRAN-lava >= 1.4.1
BuildRequires:    R-CRAN-mvtnorm >= 1.0.3
Requires:         R-CRAN-prodlim >= 1.4.9
Requires:         R-CRAN-lava >= 1.4.1
Requires:         R-CRAN-mvtnorm >= 1.0.3

%description
Estimation of two-state (survival) models and irreversible illness- death
models with possibly interval-censored, left-truncated and right-censored
data. Proportional intensities regression models can be specified to allow
for covariates effects separately for each transition. We use either a
parametric approach with Weibull baseline intensities or a semi-parametric
approach with M-splines approximation of baseline intensities in order to
obtain smooth estimates of the hazard functions. Parameter estimates are
obtained by maximum likelihood in the parametric approach and by penalized
maximum likelihood in the semi-parametric approach.

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
