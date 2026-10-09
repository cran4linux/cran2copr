%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tradesimr
%global packver   0.18.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.18.7
Release:          1%{?dist}%{?buildtag}
Summary:          Execution and Simulation Engine for Trading Strategies

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-R6 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-R6 

%description
An R-native trading simulation package with a C++ execution core that
turns strategy intentions and explicit orders into simulated trades,
positions, cash, profit and loss, risk, and performance outputs under
configurable execution, margin, funding, and cost assumptions. The package
provides historical replay, incremental exchange stepping, durable event
tables, append-only agent command logs, registered assets, per-agent
shared-cash cross-margin live accounts, AI agent competitors, scheduled
live-feed stepping, strategy-backed AI agents with diagnostics, calibrated
and coordinated multi-asset market simulation with static covariance,
AR-GARCH, factor, and regime models, durable per-feed simulation state,
profile-aware heterogeneous inventory and margin execution with atomic
mixed-profile order groups, optional portfolio-margin enforcement through
a multi-asset C++ step kernel, local live-service APIs, import/export
helpers, separate replay, live-state, and agent dashboard exports, and
installed local orchestration scripts. It is designed to consume signals,
order intents, or target exposure decisions from compatible strategy
packages and market data from compatible adapters.

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
