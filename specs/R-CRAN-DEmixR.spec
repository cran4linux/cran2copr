%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DEmixR
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Fit Two-Component Normal and Lognormal Mixture Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-DEoptim >= 2.0.0
BuildRequires:    R-CRAN-pbapply >= 1.0.0
Requires:         R-CRAN-DEoptim >= 2.0.0
Requires:         R-CRAN-pbapply >= 1.0.0

%description
Fits, bootstraps, and evaluates two-component normal and lognormal mixture
models. Parameters are estimated by combining differential-evolution
global optimization, as implemented in the 'DEoptim' package (Mullen,
Ardia, Gil, Windover and Cline, 2011) <doi:10.18637/jss.v040.i06>, with a
local 'L-BFGS-B' refinement step via optim(). Also provides preliminary
diagnostic plots, automatic normal-versus-lognormal model selection by
information criteria, and parametric or nonparametric bootstrap confidence
intervals for the fitted parameters.

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
