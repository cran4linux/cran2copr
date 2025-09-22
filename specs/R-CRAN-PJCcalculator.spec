%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PJCcalculator
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          PROs-Joint Contrast (PJC) Calculator

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-dplyr 
Requires:         R-splines 
Requires:         R-CRAN-rlang 

%description
Computes the Patient-Reported Outcomes (PROs) Joint Contrast (PJC), a
residual-based summary that captures information left over after
accounting for the clinical Disease Activity index for Psoriatic Arthritis
(cDAPSA). PROs (pain and patient global assessment) and joint counts
(swollen and tender) are standardized, then each component is adjusted for
standardized cDAPSA using natural spline coefficients that were derived
from previously published models. The resulting residuals are standardized
and combined using fixed principal component loadings, to yield a
continuous PJC score and quartile groupings. This package provides a
calculator for applying those published coefficients to new datasets; it
does not itself estimate spline models or principal components.

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
