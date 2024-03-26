%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  INLAjoint
%global packver   24.3.25
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          24.3.25
Release:          1%{?dist}%{?buildtag}
Summary:          Multivariate Joint Modeling for Longitudinal and Time-to-Event Outcomes with 'INLA'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-ggplot2 
Requires:         R-methods 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-mvtnorm 

%description
Estimation of joint models for multivariate longitudinal markers (with
various distributions available) and survival outcomes (possibly
accounting for competing risks) with Integrated Nested Laplace
Approximations (INLA). The flexible and user friendly function joint()
facilitates the use of the fast and reliable inference technique
implemented in the 'INLA' package for joint modeling. More details are
given in the help page of the joint() function (accessible via ?joint in
the R console) and the vignette associated to the joint() function
(accessible via vignette("INLAjoint") in the R console).

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
