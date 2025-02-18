%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  spinBayes
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Semi-Parametric Gene-Environment Interaction via Bayesian Variable Selection

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-testthat 
Requires:         R-CRAN-Rcpp 
Requires:         R-splines 
Requires:         R-CRAN-glmnet 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-CRAN-ggplot2 

%description
Many complex diseases are known to be affected by the interactions between
genetic variants and environmental exposures beyond the main genetic and
environmental effects. Existing Bayesian methods for gene-environment
(G×E) interaction studies are challenged by the high-dimensional nature of
the study and the complexity of environmental influences. We have
developed a novel and powerful semi-parametric Bayesian variable selection
method that can accommodate linear and nonlinear G×E interactions
simultaneously (Ren et al. (2020) <doi:10.1002/sim.8434>). Furthermore,
the proposed method can conduct structural identification by
distinguishing nonlinear interactions from main effects only case within
Bayesian framework. Spike-and-slab priors are incorporated on both
individual and group level to shrink coefficients corresponding to
irrelevant main and interaction effects to zero exactly. The Markov chain
Monte Carlo algorithms of the proposed and alternative methods are
efficiently implemented in C++.

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
