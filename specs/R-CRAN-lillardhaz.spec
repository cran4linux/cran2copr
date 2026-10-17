%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  lillardhaz
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Simultaneous-Equations Hazard/Probit Models with a Gaussian-Copula Correlation

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-maxLik 
BuildRequires:    R-CRAN-pbivnorm 
BuildRequires:    R-stats 
Requires:         R-CRAN-maxLik 
Requires:         R-CRAN-pbivnorm 
Requires:         R-stats 

%description
Fits two-equation simultaneous models in the style of Lillard (1993)
<doi:10.1016/0304-4076(93)90106-F>: a pair of processes, each either a
binary probit outcome or a continuous-time hazard duration, linked through
a single correlation parameter between their underlying error terms and
estimated jointly by maximum likelihood via a Gaussian copula. Equation 1
may be a probit, a log-normal accelerated-failure-time hazard, or a
piecewise (linear-log-hazard) Gompertz hazard with an arbitrary,
user-specified number of segments; equation 2 is always a hazard,
log-normal or piecewise Gompertz. Models can also be fit under
independence (correlation fixed at zero), which reduces exactly to two
separate univariate fits. See the package vignette/manual for the full
likelihood derivation and a simulation-based verification.

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
