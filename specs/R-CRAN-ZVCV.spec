%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ZVCV
%global packver   2.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Zero-Variance Control Variates

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.11.0
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Rlinsolve 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-Rcpp >= 0.11.0
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-mvtnorm 
Requires:         R-stats 
Requires:         R-CRAN-Rlinsolve 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-dplyr 

%description
Stein control variates can be used to improve Monte Carlo estimates of
expectations when the derivatives of the log target are available. This
package implements a variety of such methods, including zero-variance
control variates (ZV-CV, Mira et al. (2013)
<doi:10.1007/s11222-012-9344-6>), regularised ZV-CV (South et al., 2018
<arXiv:1811.05073>), control functionals (CF, Oates et al. (2017)
<doi:10.1111/rssb.12185>) and semi-exact control functionals (SECF, South
et al., 2020 <arXiv:2002.00033>). ZV-CV is a parametric approach that is
exact for (low order) polynomial integrands with Gaussian targets. CF is a
non-parametric alternative that offers better than the standard Monte
Carlo convergence rates. SECF has both a parametric and a non-parametric
component and it offers the advantages of both for an additional
computational cost. Functions for applying ZV-CV and CF to two estimators
for the normalising constant of the posterior distribution in Bayesian
statistics are also supplied in this package. The basic requirements for
using the package are a set of samples, derivatives and function
evaluations.

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
