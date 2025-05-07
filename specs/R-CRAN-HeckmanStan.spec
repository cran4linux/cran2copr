%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  HeckmanStan
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Heckman Selection Models Based on Bayesian Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rstan >= 2.26.23
BuildRequires:    R-CRAN-mvtnorm >= 1.2.3
BuildRequires:    R-CRAN-loo 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-rstantools
Requires:         R-CRAN-rstan >= 2.26.23
Requires:         R-CRAN-mvtnorm >= 1.2.3
Requires:         R-CRAN-loo 
Requires:         R-stats 
Requires:         R-CRAN-rstantools

%description
Implements Heckman selection models using a Bayesian approach via 'Stan'
and compares the performance of normal, Student’s t, and contaminated
normal distributions in addressing complexities and selection bias (Heeju
Lim, Victor E. Lachos, and Victor H. Lachos, Bayesian analysis of flexible
Heckman selection models using Hamiltonian Monte Carlo, 2025, under
submission).

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
