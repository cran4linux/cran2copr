%global __brp_check_rpaths %{nil}
%global packname  Bayesrel
%global packver   0.7.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.4
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Reliability Estimation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-Rcpp >= 1.0.4.6
BuildRequires:    R-CRAN-LaplacesDemon 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-lavaan 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 1.0.4.6
Requires:         R-CRAN-LaplacesDemon 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-lavaan 
Requires:         R-CRAN-coda 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-Rdpack 

%description
Functionality for reliability estimates. For 'unidimensional' tests:
Coefficient alpha, 'Guttman's' lambda-2/-4/-6, the Greatest lower bound
and coefficient omega_u ('unidimensional') in a Bayesian and a frequentist
version. For multidimensional tests: omega_t (total) and omega_h
(hierarchical). The results include confidence and credible intervals, the
probability of a coefficient being larger than a cutoff, and a check for
the factor models, necessary for the omega coefficients. The method for
the Bayesian 'unidimensional' estimates, except for omega_u, is sampling
from the posterior inverse 'Wishart' for the covariance matrix based
measures (see 'Murphy', 2007,
<https://groups.seas.harvard.edu/courses/cs281/papers/murphy-2007.pdf>.
The Bayesian omegas (u, t, and h) are obtained by 'Gibbs' sampling from
the conditional posterior distributions of (1) the single factor model and
(2) the second-order factor model ('Lee', 2007,
<https://onlinelibrary.wiley.com/doi/book/10.1002/9780470024737>).

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
