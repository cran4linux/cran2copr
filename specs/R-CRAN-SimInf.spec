%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SimInf
%global packver   9.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          9.6.0
Release:          1%{?dist}%{?buildtag}
Summary:          A Framework for Data-Driven Stochastic Disease Spread Simulations

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    gsl-devel
BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildRequires:    R-CRAN-Matrix >= 1.3.0
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-Matrix >= 1.3.0
Requires:         R-CRAN-digest 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-MASS 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 

%description
Provides an efficient and very flexible framework to conduct data-driven
epidemiological modeling in realistic large scale disease spread
simulations. The framework integrates infection dynamics in subpopulations
as continuous-time Markov chains using the Gillespie stochastic simulation
algorithm and incorporates available data such as births, deaths and
movements as scheduled events at predefined time-points. Using C code for
the numerical solvers and 'OpenMP' (if available) to divide work over
multiple processors ensures high performance when simulating a sample
outcome. One of our design goals was to make the package extendable and
enable usage of the numerical solvers from other R extension packages in
order to facilitate complex epidemiological research. The package contains
template models and can be extended with user-defined models. For more
details see the paper by Widgren, Bauer, Eriksson and Engblom (2019)
<doi:10.18637/jss.v091.i12>. The package also provides functionality to
fit models to time series data using the Approximate Bayesian Computation
Sequential Monte Carlo ('ABC-SMC') algorithm of Toni and others (2009)
<doi:10.1098/rsif.2008.0172>.

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
