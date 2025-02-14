%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sgdGMF
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Estimation of Generalized Matrix Factorization Models via Stochastic Gradient Descent

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.10
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-RSpectra 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-SuppDists 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-viridisLite 
Requires:         R-CRAN-Rcpp >= 1.0.10
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-RcppArmadillo 
Requires:         R-CRAN-RSpectra 
Requires:         R-parallel 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-SuppDists 
Requires:         R-methods 
Requires:         R-CRAN-generics 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-viridisLite 

%description
Efficient framework to estimate high-dimensional generalized matrix
factorization models using penalized maximum likelihood under a dispersion
exponential family specification. Either deterministic and stochastic
methods are implemented for the numerical maximization. In particular, the
package implements the stochastic gradient descent algorithm with a
block-wise mini-batch strategy to speed up the computations and an
efficient adaptive learning rate schedule to stabilize the convergence.
All the theoretical details can be found in Castiglione et al. (2024,
<doi:10.48550/arXiv.2412.20509>). Other methods considered for the
optimization are the alternated iterative re-weighted least squares and
the quasi-Newton method with diagonal approximation of the Fisher
information matrix discussed in Kidzinski et al. (2022,
<http://jmlr.org/papers/v23/20-1104.html>).

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
