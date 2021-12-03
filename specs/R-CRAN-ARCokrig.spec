%global __brp_check_rpaths %{nil}
%global packname  ARCokrig
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Autoregressive Cokriging Models for Multifidelity Codes

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-mvtnorm >= 1.0.10
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-mvtnorm >= 1.0.10
Requires:         R-CRAN-Rcpp 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-CRAN-ggplot2 

%description
For emulating multifidelity computer models. The major methods include
univariate autoregressive cokriging and multivariate autoregressive
cokriging. The autoregressive cokriging methods are implemented for both
hierarchically nested design and non-nested design. For hierarchically
nested design, the model parameters are estimated via standard
optimization algorithms; For non-nested design, the model parameters are
estimated via Monte Carlo expectation-maximization (MCEM) algorithms. In
both cases, the priors are chosen such that the posterior distributions
are proper. Notice that the uniform priors on range parameters in the
correlation function lead to improper posteriors. This should be avoided
when Bayesian analysis is adopted. The development of objective priors for
autoregressive cokriging models can be found in Pulong Ma (2020)
<DOI:10.1137/19M1289893>. The development of the multivariate
autoregressive cokriging models with possibly non-nested design can be
found in Pulong Ma, Georgios Karagiannis, Bledar A Konomi, Taylor G Asher,
Gabriel R Toro, and Andrew T Cox (2019) <arXiv:1909.01836>.

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
