%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sbwadjust
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Stable Balancing Weights for Covariate Adjustment in Trials

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-survival 
Requires:         R-graphics 
Requires:         R-CRAN-quadprog 
Requires:         R-stats 
Requires:         R-CRAN-survival 

%description
Covariate adjustment for randomized trials using stable balancing weights
(SBW), as proposed by Irish, Zubizarreta, and Luedtke (2026)
<doi:10.48550/arXiv.2609.01638>. sbw_weights() fits exact-balance SBW for
a two-arm study by a closed-form solve with a nonnegative
quadratic-programming fallback; sbw_estimate() computes a closed menu of
treatment-effect estimands (average treatment effect, relative risk,
survival ratio, Mann-Whitney, quantile contrasts) from the fitted weights,
with bootstrap confidence intervals.

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
