%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ordinal
%global packver   2025.12-29
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2025.12.29
Release:          1%{?dist}%{?buildtag}
Summary:          Regression Models for Ordinal Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.13.0
Requires:         R-core >= 2.13.0
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-ucminf 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-nlme 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-CRAN-ucminf 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-nlme 

%description
Implementation of cumulative link (mixed) models also known as ordered
regression models, proportional odds models, proportional hazards models
for grouped survival times and ordered logit/probit/... models. Estimation
is via maximum likelihood and mixed models are fitted with the Laplace
approximation and adaptive Gauss-Hermite quadrature. Multiple random
effect terms are allowed and they may be nested, crossed or partially
nested/crossed. Restrictions of symmetry and equidistance can be imposed
on the thresholds (cut-points/intercepts). Standard model methods are
available (summary, anova, drop-methods, step, confint, predict etc.) in
addition to profile methods and slice methods for visualizing the
likelihood function and checking convergence.

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
