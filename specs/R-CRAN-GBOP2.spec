%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  GBOP2
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Generalized Bayesian Optimal Phase II Design (G-BOP2)

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-globpso 
BuildRequires:    R-parallel 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-dplyr 
Requires:         R-stats 
Requires:         R-CRAN-globpso 
Requires:         R-parallel 
Requires:         R-utils 
Requires:         R-CRAN-RcppArmadillo 

%description
Provides functions for implementing the Generalized Bayesian Optimal Phase
II (G-BOP2) design using various Particle Swarm Optimization (PSO)
algorithms, including: - PSO-Default, based on Kennedy and Eberhart (1995)
<doi:10.1109/ICNN.1995.488968>, "Particle Swarm Optimization"; -
PSO-Quantum, based on Sun, Xu, and Feng (2004)
<doi:10.1109/ICCIS.2004.1460396>, "A Global Search Strategy of
Quantum-Behaved Particle Swarm Optimization"; - PSO-Dexp, based on Stehlík
et al. (2024) <doi:10.1016/j.asoc.2024.111913>, "A Double Exponential
Particle Swarm Optimization with Non-Uniform Variates as Stochastic Tuning
and Guaranteed Convergence to a Global Optimum with Sample Applications to
Finding Optimal Exact Designs in Biostatistics"; - and PSO-GO.

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
