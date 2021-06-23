%global __brp_check_rpaths %{nil}
%global packname  runexp
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Softball Run Expectancy using Markov Chains and Simulation

License:          LGPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-parallel 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-parallel 

%description
Implements two methods of estimating runs scored in a softball scenario:
(1) theoretical expectation using discrete Markov chains and (2) empirical
distribution using multinomial random simulation.  Scores are based on
player-specific input probabilities (out, single, double, triple, walk,
and homerun).  Optional inputs include probability of attempting a steal,
probability of succeeding in an attempted steal, and an indicator of
whether a player is "fast" (e.g. the player could stretch home).  These
probabilities may be calculated from common player statistics that are
publicly available on team's webpages. Scores are evaluated based on a
nine-player lineup and may be used to compare lineups, evaluate base
scenarios, and compare the offensive potential of individual players.
Manuscript forthcoming.  See Bukiet & Harold (1997)
<doi:10.1287/opre.45.1.14> for implementation of discrete Markov chains.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
