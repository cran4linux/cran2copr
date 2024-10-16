%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  IBMPopSim
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Individual Based Model Population Simulation

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-dplyr >= 0.8.0
BuildRequires:    R-CRAN-Rcpp >= 0.12
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-dplyr >= 0.8.0
Requires:         R-CRAN-Rcpp >= 0.12
Requires:         R-CRAN-checkmate 
Requires:         R-stats 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-ggplot2 

%description
Simulation of the random evolution of heterogeneous populations using
stochastic Individual-Based Models (IBMs) <doi:10.48550/arXiv.2303.06183>.
The package enables users to simulate population evolution, in which
individuals are characterized by their age and some characteristics, and
the population is modified by different types of events, including
births/arrivals, death/exit events, or changes of characteristics. The
frequency at which an event can occur to an individual can depend on their
age and characteristics, but also on the characteristics of other
individuals (interactions). Such models have a wide range of applications.
For instance, IBMs can be used for simulating the evolution of a
heterogeneous insurance portfolio with selection or for validating
mortality forecasts. This package overcomes the limitations of
time-consuming IBMs simulations by implementing new efficient algorithms
based on thinning methods, which are compiled using the 'Rcpp' package
while providing a user-friendly interface.

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
