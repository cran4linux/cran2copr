%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  StochSimR
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Stochastic Process Simulation Engine

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-future >= 1.25.0
BuildRequires:    R-CRAN-future.apply >= 1.10.0
BuildRequires:    R-CRAN-rlang >= 1.0.0
BuildRequires:    R-stats 
BuildRequires:    R-parallel 
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-future >= 1.25.0
Requires:         R-CRAN-future.apply >= 1.10.0
Requires:         R-CRAN-rlang >= 1.0.0
Requires:         R-stats 
Requires:         R-parallel 

%description
A modular simulation engine for a wide range of stochastic processes.
Provides exact and approximate simulation methods for Poisson processes
(homogeneous and inhomogeneous), Brownian motion (standard, drifted, and
bridge), discrete- and continuous-time Markov chains, birth-death
processes, the Yule pure-birth process, infinitesimal generator matrix
utilities, Markovian queuing systems (M/M/1, M/M/c, M/M/c/K) with exact
steady-state statistics, Levy processes (gamma, normal inverse Gaussian,
variance-gamma, alpha-stable), Merton jump-diffusion models, Hawkes
self-exciting processes, geometric Brownian motion, and Ornstein-Uhlenbeck
mean-reverting diffusions. Includes variance reduction techniques
(antithetic variates, control variates, importance sampling, stratified
sampling), parallel simulation via the 'future' framework, rare-event
simulation (cross-entropy and multilevel splitting), path visualisation,
and summary statistics. Methods are based on Glasserman (2003)
<doi:10.1007/978-0-387-21617-1>, Asmussen & Glynn (2007)
<doi:10.1007/978-0-387-69033-9>, Norris (1997)
<doi:10.1017/CBO9780511810633>, and Kleinrock (1975, ISBN:0471491101).

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
