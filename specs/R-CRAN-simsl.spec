%global packname  simsl
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Single-Index Models with a Surface-Link

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-stats 
Requires:         R-CRAN-mgcv 
Requires:         R-stats 

%description
An implementation of a single-index regression for optimizing
individualized dose rules from an observational study. To model
interaction effects between baseline covariates and a treatment variable
defined on a continuum, we employ two-dimensional penalized spline
regression on an index-treatment domain, where the index is defined as a
linear combination of the covariates (a single-index). An unspecified main
effect for the covariates is allowed, which can also be modeled through a
parametric model. A unique contribution of this work is in the
parsimonious single-index parametrization specifically defined for the
interaction effect term. We refer to Park, Petkova, Tarpey, and Ogden
(2020) <doi:10.1111/biom.13320> (for the case of a discrete treatment) and
Park, Petkova, Tarpey, and Ogden (2021) "A single-index model with a
surface-link for optimizing individualized dose rules"
<arXiv:2006.00267v2> for detail of the method. The model can take a member
of the exponential family as a response variable and can also take an
ordinal categorical response. The main function of this package is
simsl().

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
