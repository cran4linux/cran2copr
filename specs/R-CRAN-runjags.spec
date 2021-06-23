%global __brp_check_rpaths %{nil}
%global packname  runjags
%global packver   2.2.0-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Interface Utilities, Model Templates, Parallel Computing Methods and Additional Distributions for MCMC Models in JAGS

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    jags-devel
BuildRequires:    R-devel >= 2.14.0
Requires:         R-core >= 2.14.0
BuildRequires:    R-CRAN-lattice >= 0.20.10
BuildRequires:    R-CRAN-coda >= 0.17.1
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-lattice >= 0.20.10
Requires:         R-CRAN-coda >= 0.17.1
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-utils 

%description
User-friendly interface utilities for MCMC models via Just Another Gibbs
Sampler (JAGS), facilitating the use of parallel (or distributed)
processors for multiple chains, automated control of convergence and
sample length diagnostics, and evaluation of the performance of a model
using drop-k validation or against simulated data. Template model
specifications can be generated using a standard lme4-style formula
interface to assist users less familiar with the BUGS syntax.  A JAGS
extension module provides additional distributions including the Pareto
family of distributions, the DuMouchel prior and the half-Cauchy prior.

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
