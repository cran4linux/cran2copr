%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PLMIX
%global packver   2.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Analysis of Finite Mixture of Plackett-Luce Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-gridExtra >= 2.3
BuildRequires:    R-CRAN-ggplot2 >= 2.2.1
BuildRequires:    R-CRAN-label.switching >= 1.6
BuildRequires:    R-CRAN-abind >= 1.4.5
BuildRequires:    R-CRAN-foreach >= 1.4.4
BuildRequires:    R-CRAN-reshape2 >= 1.4.3
BuildRequires:    R-CRAN-MCMCpack >= 1.4.2
BuildRequires:    R-CRAN-ggmcmc >= 1.2
BuildRequires:    R-CRAN-rcdd >= 1.2
BuildRequires:    R-CRAN-Rcpp >= 1.0.5
BuildRequires:    R-CRAN-radarchart >= 0.3.1
BuildRequires:    R-CRAN-PlackettLuce >= 0.2.3
BuildRequires:    R-CRAN-coda >= 0.19.1
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-gridExtra >= 2.3
Requires:         R-CRAN-ggplot2 >= 2.2.1
Requires:         R-CRAN-label.switching >= 1.6
Requires:         R-CRAN-abind >= 1.4.5
Requires:         R-CRAN-foreach >= 1.4.4
Requires:         R-CRAN-reshape2 >= 1.4.3
Requires:         R-CRAN-MCMCpack >= 1.4.2
Requires:         R-CRAN-ggmcmc >= 1.2
Requires:         R-CRAN-rcdd >= 1.2
Requires:         R-CRAN-Rcpp >= 1.0.5
Requires:         R-CRAN-radarchart >= 0.3.1
Requires:         R-CRAN-PlackettLuce >= 0.2.3
Requires:         R-CRAN-coda >= 0.19.1
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 

%description
Fit finite mixtures of Plackett-Luce models for partial top
rankings/orderings within the Bayesian framework. It provides MAP point
estimates via EM algorithm and posterior MCMC simulations via Gibbs
Sampling. It also fits MLE as a special case of the noninformative
Bayesian analysis with vague priors. In addition to inferential
techniques, the package assists other fundamental phases of a model-based
analysis for partial rankings/orderings, by including functions for data
manipulation, simulation, descriptive summary, model selection and
goodness-of-fit evaluation. Main references on the methods are Mollica and
Tardella (2017) <doi:10.1007/s11336-016-9530-0> and Mollica and Tardella
(2014) <doi:10.1002/sim.6224>.

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
