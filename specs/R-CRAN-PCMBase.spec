%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PCMBase
%global packver   1.2.15
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.15
Release:          1%{?dist}%{?buildtag}
Summary:          Simulation and Likelihood Calculation of Phylogenetic Comparative Models

License:          GPL (>= 3.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-expm 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-xtable 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-expm 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-xtable 

%description
Phylogenetic comparative methods represent models of continuous trait data
associated with the tips of a phylogenetic tree. Examples of such models
are Gaussian continuous time branching stochastic processes such as
Brownian motion (BM) and Ornstein-Uhlenbeck (OU) processes, which regard
the data at the tips of the tree as an observed (final) state of a Markov
process starting from an initial state at the root and evolving along the
branches of the tree. The PCMBase R package provides a general framework
for manipulating such models. This framework consists of an application
programming interface for specifying data and model parameters, and
efficient algorithms for simulating trait evolution under a model and
calculating the likelihood of model parameters for an assumed model and
trait data. The package implements a growing collection of models, which
currently includes BM, OU, BM/OU with jumps, two-speed OU as well as mixed
Gaussian models, in which different types of the above models can be
associated with different branches of the tree. The PCMBase package is
limited to trait-simulation and likelihood calculation of (mixed) Gaussian
phylogenetic models. The PCMFit package provides functionality for
inference of these models to tree and trait data. The package web-site
<https://venelin.github.io/PCMBase/> provides access to the documentation
and other resources.

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
