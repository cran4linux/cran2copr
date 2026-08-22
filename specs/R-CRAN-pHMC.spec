%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pHMC
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Proximal Hamiltonian Monte Carlo for Non-Smooth Bayesian Inference

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-Matrix 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-utils 
Requires:         R-CRAN-Matrix 

%description
Implements the Proximal Hamiltonian Monte Carlo (p-HMC) algorithm for
Bayesian sampling and estimation from non-differentiable target densities.
The method decomposes a target potential into a smooth component f(x) and
a non-smooth convex component g(x), approximating only g(x) via its
Moreau-Yosida envelope while retaining exact gradient information for
f(x). This approach, based on the methodology described in Shukla, Vats,
and Chi (2025) <doi:10.48550/arXiv.2510.22252>, yields improved
Hamiltonian conservation over full-potential smoothing approaches. The
package provides generalized routines accepting user-defined probability
density functions, log-likelihoods, priors, and proximal operators,
together with automated hyperparameter tuning for the Moreau-Yosida
regularization parameter, Markov chain Monte Carlo convergence
diagnostics, effective sample size computation, and model evaluation
metrics including the Akaike information criterion and Bayesian
information criterion.

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
