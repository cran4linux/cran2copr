%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  evoper
%global packver   0.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.0
Release:          1%{?dist}%{?buildtag}
Summary:          Evolutionary Parameter Estimation for 'Repast Simphony' Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-rrepast 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-logging 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-reshape 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-deSolve 
BuildRequires:    R-CRAN-plot3D 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RNetLogo 
Requires:         R-CRAN-rrepast 
Requires:         R-methods 
Requires:         R-CRAN-logging 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-reshape 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-deSolve 
Requires:         R-CRAN-plot3D 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-data.table 
Requires:         R-utils 
Requires:         R-CRAN-RNetLogo 

%description
The EvoPER, Evolutionary Parameter Estimation for Individual-based Models
is an extensible package providing optimization driven parameter
estimation methods using metaheuristics and evolutionary computation
techniques (Particle Swarm Optimization, Simulated Annealing, Ant Colony
Optimization for continuous domains, Tabu Search, Evolutionary Strategies,
...)  which could be more efficient and require, in some cases, fewer
model evaluations than alternatives relying on experimental design.
Currently there are built in support for models developed with 'Repast
Simphony' Agent-Based framework (<https://repast.github.io/>) and with
NetLogo (<https://www.netlogo.org/>) which are the most used frameworks
for Agent-based modeling.

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
