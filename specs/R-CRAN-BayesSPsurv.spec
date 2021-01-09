%global packname  BayesSPsurv
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Spatial Split Population Survival Model

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.3
BuildRequires:    R-CRAN-MCMCpack 
BuildRequires:    R-CRAN-FastGP 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 1.0.3
Requires:         R-CRAN-MCMCpack 
Requires:         R-CRAN-FastGP 
Requires:         R-stats 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ape 

%description
Parametric spatial split-population (SP) survival models for clustered
event processes. The models account for structural and spatial
heterogeneity among “at risk” and “immune” populations, and incorporate
time-varying covariates. This package currently implements Weibull,
Exponential and Log-logistic forms for the duration component. It also
includes functions for a series of diagnostic tests and plots to easily
visualize spatial autocorrelation, convergence, and spatial effects. Users
can create their own spatial weights matrix based on their units and
adjacencies of interest, making the use of these models flexible and
broadly applicable to a variety of research areas. Joo et al. (2020)
<https://github.com/Nicolas-Schmidt/BayesSPsurv/blob/master/man/figures/SPcure.pdf>
describe the estimators included in this package.

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
