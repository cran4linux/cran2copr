%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  finlabR
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Portfolio Analytics and Simulation Toolkit

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-PerformanceAnalytics 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-class 
BuildRequires:    R-CRAN-quantmod 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-CRAN-shiny 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-quadprog 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-PerformanceAnalytics 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-class 
Requires:         R-CRAN-quantmod 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-mclust 
Requires:         R-CRAN-shiny 

%description
Tools for portfolio construction and risk analytics, including
mean-variance optimization, conditional value at risk (expected shortfall)
minimization, risk parity, regime clustering, correlation analysis, Monte
Carlo simulation, and option pricing. Includes utilities for portfolio
evaluation, clustering, and risk reporting. Methods are based in part on
Markowitz (1952) <doi:10.1111/j.1540-6261.1952.tb01525.x>, Rockafellar and
Uryasev (2000) <doi:10.21314/JOR.2000.038>, Maillard et al. (2010)
<doi:10.3905/jpm.2010.36.4.060>, Black and Scholes (1973)
<doi:10.1086/260062>, and Cox et al. (1979)
<doi:10.1016/0304-405X(79)90015-1>.

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
