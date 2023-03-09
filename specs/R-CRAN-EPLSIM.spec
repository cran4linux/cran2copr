%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  EPLSIM
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Partial Linear Single Index Models for Environmental Mixture Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-ciTools 
Requires:         R-splines 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-ciTools 

%description
Collection of ancillary functions and utilities for Partial Linear Single
Index Models for Environmental mixture analyses, which currently provides
functions for scalar outcomes. The outputs of these functions include the
single index function, single index coefficients, partial linear
coefficients, mixture overall effect, exposure main and interaction
effects, and differences of quartile effects. In the future, we will add
functions for binary, ordinal, Poisson, survival, and longitudinal
outcomes, as well as models for time-dependent exposures. See Wang et al
(2020) <doi:10.1186/s12940-020-00644-4> for an overview.

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
