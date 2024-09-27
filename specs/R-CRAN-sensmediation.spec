%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sensmediation
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Parametric Estimation and Sensitivity Analysis of Direct and Indirect Effects

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-maxLik >= 1.3.4
BuildRequires:    R-CRAN-mvtnorm >= 1.0.8
BuildRequires:    R-stats 
Requires:         R-CRAN-maxLik >= 1.3.4
Requires:         R-CRAN-mvtnorm >= 1.0.8
Requires:         R-stats 

%description
We implement functions to estimate and perform sensitivity analysis to
unobserved confounding of direct and indirect effects introduced in
Lindmark, de Luna and Eriksson (2018) <doi:10.1002/sim.7620> and Lindmark
(2022) <doi:10.1007/s10260-021-00611-4>. The estimation and sensitivity
analysis are parametric, based on probit and/or linear regression models.
Sensitivity analysis is implemented for unobserved confounding of the
exposure-mediator, mediator-outcome and exposure-outcome relationships.

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
