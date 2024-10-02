%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rbw
%global packver   0.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.2
Release:          1%{?dist}%{?buildtag}
Summary:          Residual Balancing Weights for Marginal Structural Models

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr >= 0.8.4
BuildRequires:    R-CRAN-rlang >= 0.4.4
BuildRequires:    R-stats 
Requires:         R-CRAN-dplyr >= 0.8.4
Requires:         R-CRAN-rlang >= 0.4.4
Requires:         R-stats 

%description
Residual balancing is a robust method of constructing weights for marginal
structural models, which can be used to estimate (a) the average treatment
effect in a cross-sectional observational study, (b) controlled
direct/mediator effects in causal mediation analysis, and (c) the effects
of time-varying treatments in panel data (Zhou and Wodtke 2020
<doi:10.1017/pan.2020.2>). This package provides three functions,
rbwPoint(), rbwMed(), and rbwPanel(), that produce residual balancing
weights for estimating (a), (b), (c), respectively.

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
