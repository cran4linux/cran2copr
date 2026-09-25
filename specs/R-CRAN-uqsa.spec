%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  uqsa
%global packver   0.8.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.0
Release:          1%{?dist}%{?buildtag}
Summary:          Uncertainty Quantification and Global Sensitivity Analysis

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-Ryacas 
BuildRequires:    R-CRAN-VineCopula 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-errors 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-cli 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-CRAN-Ryacas 
Requires:         R-CRAN-VineCopula 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-errors 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-colorspace 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-cli 

%description
In the field of systems biology, chemical reaction networks are modeled in
various ways, two of those are: (i) stochastic simulations (e.g. Gillespie
algorithm) and (ii) ordinary differential equations. In this package we
use a simple tabular model description of reaction systems and
automatically generate C code for either solver type. We use the ordinary
differential equation solvers from the GNU Scientific Library and provide
an interface that deals with lists of simulation experiments. Each
simulation experiment contains both the data, and instructions for the
model to replicate the data. We use approximate Bayesian computation
methods (combined with Markov chain Monte Carlo and sequential Monte
Carlo, particle filters) as well as classic methods such as Random Walk
Metropolis (Gaussian transition kernel) and Simplified Manifold Metropolis
adjusted Langevin algorithm for a Bayesian investigation of the model´s
parameter space. Experiments can be evaluated in a sequence; intermediate
probability densities are modeled using the 'VineCopula' package. The
package is also intended to be useful in an HPC environment, with some
functions that use 'pbdMPI' capabilities.

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
