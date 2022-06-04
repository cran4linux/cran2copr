%global __brp_check_rpaths %{nil}
%global packname  coxme
%global packver   2.2-17
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.17
Release:          1%{?dist}%{?buildtag}
Summary:          Mixed Effects Cox Models

License:          LGPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-survival >= 2.36.14
BuildRequires:    R-CRAN-bdsmatrix >= 1.3
BuildRequires:    R-CRAN-Matrix >= 1.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-nlme 
Requires:         R-CRAN-survival >= 2.36.14
Requires:         R-CRAN-bdsmatrix >= 1.3
Requires:         R-CRAN-Matrix >= 1.0
Requires:         R-methods 
Requires:         R-CRAN-nlme 

%description
Fit Cox proportional hazards models containing both fixed and random
effects.  The random effects can have a general form, of which familial
interactions (a "kinship" matrix) is a particular special case. Note that
the simplest case of a mixed effects Cox model, i.e. a single random
per-group intercept, is also called a "frailty" model.  The approach is
based on Ripatti and Palmgren, Biometrics 2002.

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
