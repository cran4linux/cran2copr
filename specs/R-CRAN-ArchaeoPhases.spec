%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ArchaeoPhases
%global packver   2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Post-Processing of Markov Chain Monte Carlo Simulations for Chronological Modelling

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-arkhe >= 1.6.0
BuildRequires:    R-CRAN-aion >= 1.0.2
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-arkhe >= 1.6.0
Requires:         R-CRAN-aion >= 1.0.2
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-tools 
Requires:         R-utils 

%description
Statistical analysis of archaeological dates and groups of dates. This
package allows to post-process Markov Chain Monte Carlo (MCMC) simulations
from 'ChronoModel' <https://chronomodel.com/>, 'Oxcal'
<https://c14.arch.ox.ac.uk/oxcal.html> or 'BCal'
<https://bcal.shef.ac.uk/>. It provides functions for the study of rhythms
of the long term from the posterior distribution of a series of dates
(tempo and activity plot). It also allows the estimation and visualization
of time ranges from the posterior distribution of groups of dates (e.g.
duration, transition and hiatus between successive phases) as described in
Philippe and Vibet (2020) <doi:10.18637/jss.v093.c01>.

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
