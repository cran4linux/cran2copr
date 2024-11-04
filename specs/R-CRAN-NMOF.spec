%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  NMOF
%global packver   2.10-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.10.1
Release:          1%{?dist}%{?buildtag}
Summary:          Numerical Methods and Optimization in Finance

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-utils 

%description
Functions, examples and data from the first and the second edition of
"Numerical Methods and Optimization in Finance" by M. Gilli, D. Maringer
and E. Schumann (2019, ISBN:978-0128150658).  The package provides
implementations of optimisation heuristics (Differential Evolution,
Genetic Algorithms, Particle Swarm Optimisation, Simulated Annealing and
Threshold Accepting), and other optimisation tools, such as grid search
and greedy search.  There are also functions for the valuation of
financial instruments such as bonds and options, for portfolio selection
and functions that help with stochastic simulations.

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
