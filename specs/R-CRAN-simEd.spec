%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  simEd
%global packver   2.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Simulation Education

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-rstream 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-shape 
Requires:         R-CRAN-rstream 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-shape 

%description
Contains various functions to be used for simulation education, including
simple Monte Carlo simulation functions, queueing simulation functions,
variate generation functions capable of producing independent streams and
antithetic variates, functions for illustrating random variate generation
for various discrete and continuous distributions, and functions to
compute time-persistent statistics.  Also contains functions for
visualizing: event-driven details of a single-server queue model; a Lehmer
random number generator; variate generation via acceptance-rejection; and
of generating a non-homogeneous Poisson process via thinning.  Also
contains two queueing data sets (one fabricated, one real-world) to
facilitate input modeling.  More details on the use of these functions can
be found in Lawson and Leemis (2015) <doi:10.1109/WSC.2017.8248124>, in
Kudlay, Lawson, and Leemis (2020) <doi:10.1109/WSC48552.2020.9384010>, and
in Lawson and Leemis (2021) <doi:10.1109/WSC52266.2021.9715299>.

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
