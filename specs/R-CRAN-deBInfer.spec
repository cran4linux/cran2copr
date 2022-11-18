%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  deBInfer
%global packver   0.4.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.4
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Inference for Differential Equations

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-deSolve 
BuildRequires:    R-CRAN-truncdist 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-PBSddesolve 
BuildRequires:    R-methods 
Requires:         R-CRAN-deSolve 
Requires:         R-CRAN-truncdist 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-MASS 
Requires:         R-stats 
Requires:         R-CRAN-mvtnorm 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-PBSddesolve 
Requires:         R-methods 

%description
A Bayesian framework for parameter inference in differential equations.
This approach offers a rigorous methodology for parameter inference as
well as modeling the link between unobservable model states and
parameters, and observable quantities. Provides templates for the DE
model, the observation model and data likelihood, and the model parameters
and their prior distributions. A Markov chain Monte Carlo (MCMC) procedure
processes these inputs to estimate the posterior distributions of the
parameters and any derived quantities, including the model trajectories.
Further functionality is provided to facilitate MCMC diagnostics and the
visualisation of the posterior distributions of model parameters and
trajectories.

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
