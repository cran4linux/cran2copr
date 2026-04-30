%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  enrichwith
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          1%{?dist}%{?buildtag}
Summary:          Methods to Enrich R Objects with Extra Components

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch

%description
Provides the "enrich()" method for augmenting list-like R objects with
additional, model-specific components. Methods are currently available for
objects of class "family", "link-glm", "lm", "glm", and "betareg".
Enriched objects retain their original class and remain compatible with
existing methods. For example, enriching a "glm" object produces an
"enriched_glm" object that also inherits from "glm". In addition to the
standard components, the "enriched_glm" object includes methods for
simulation and functions to compute scores, observed and expected
information matrices, first-order bias, and other model quantities such as
densities, probabilities, and quantiles, which can be evaluated at
use-supplied parameter values. The package also provides tools for
generating customizable source code templates for the structured
implementation of methods to compute new components and enrich arbitrary
objects.

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
