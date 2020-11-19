%global packname  bayesGAM
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Fit Multivariate Response Generalized Additive Models using Hamiltonian Monte Carlo

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildRequires:    R-CRAN-RcppParallel >= 5.0.1
BuildRequires:    R-CRAN-rstan >= 2.18.1
BuildRequires:    R-CRAN-StanHeaders >= 2.18.0
BuildRequires:    R-CRAN-rstantools >= 2.1.0.9000
BuildRequires:    R-CRAN-BH >= 1.66.0
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.3.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.0
BuildRequires:    R-CRAN-bayesplot 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-corrplot 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-loo 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-mlbench 
BuildRequires:    R-CRAN-SemiPar 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-geometry 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-rstantools
Requires:         R-CRAN-RcppParallel >= 5.0.1
Requires:         R-CRAN-rstan >= 2.18.1
Requires:         R-CRAN-rstantools >= 2.1.0.9000
Requires:         R-CRAN-Rcpp >= 0.12.0
Requires:         R-CRAN-bayesplot 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-corrplot 
Requires:         R-CRAN-ggplot2 
Requires:         R-graphics 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-loo 
Requires:         R-methods 
Requires:         R-CRAN-mlbench 
Requires:         R-CRAN-SemiPar 
Requires:         R-stats 
Requires:         R-CRAN-geometry 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-rstantools

%description
The 'bayesGAM' package is designed to provide a user friendly option to
fit univariate and multivariate response Generalized Additive Models (GAM)
using Hamiltonian Monte Carlo (HMC) with few technical burdens.  The
functions in this package use 'rstan' (Stan Development Team 2020) to call
'Stan' routines that run the HMC simulations. The 'Stan' code for these
models is already pre-compiled for the user. The programming formulation
for models in 'bayesGAM' is designed to be familiar to analysts who fit
statistical models in 'R'. Carpenter, B., Gelman, A., Hoffman, M. D., Lee,
D., Goodrich, B., Betancourt, M., ... & Riddell, A. (2017). Stan: A
probabilistic programming language. Journal of statistical software,
76(1). Stan Development Team. 2018. RStan: the R interface to Stan. R
package version 2.17.3.  <https://mc-stan.org/> Neal, Radford (2011)
"Handbook of Markov Chain Monte Carlo" ISBN: 978-1420079418. Betancourt,
Michael, and Mark Girolami. "Hamiltonian Monte Carlo for hierarchical
models." Current trends in Bayesian methodology with applications 79.30
(2015): 2-4. Thomas, S., Tu, W. (2020) "Learning Hamiltonian Monte Carlo
in R" <arXiv:2006.16194>, Gelman, A., Carlin, J. B., Stern, H. S., Dunson,
D. B., Vehtari, A., & Rubin, D. B. (2013) "Bayesian Data Analysis" ISBN:
978-1439840955, Agresti, Alan (2015) "Foundations of Linear and
Generalized Linear Models ISBN: 978-1118730034, Pinheiro, J., Bates, D.
(2006) "Mixed-effects Models in S and S-Plus" ISBN: 978-1441903174.
Ruppert, D., Wand, M. P., & Carroll, R. J. (2003). Semiparametric
regression (No. 12). Cambridge university press. ISBN: 978-0521785167.

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
