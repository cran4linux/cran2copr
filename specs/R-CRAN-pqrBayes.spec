%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pqrBayes
%global packver   1.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.4
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Penalized Quantile Regression

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-splines 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-glmnet 
Requires:         R-splines 
Requires:         R-stats 

%description
Bayesian regularized quantile regression utilizing sparse priors to
promote exact sparsity leads to efficient Bayesian shrinkage estimation,
variable selection and statistical inference. In this package, we have
implemented robust Bayesian variable selection with spike-and-slab priors
under high-dimensional linear regression models (Fan et al. (2024)
<doi:10.3390/e26090794> and Ren et al. (2023) <doi:10.1111/biom.13670>),
and regularized quantile varying coefficient models (Zhou et al.(2023)
<doi:10.1016/j.csda.2023.107808>). In particular, valid robust Bayesian
inferences under both models in the presence of heavy-tailed errors can be
validated on finite samples. Additional models with spike-and-slab priors
include robust Bayesian group LASSO and robust binary Bayesian LASSO (Fan
and Wu (2025) <doi:10.1002/sta4.70078>). The Markov Chain Monte Carlo
(MCMC) algorithms of the proposed and alternative models are implemented
in C++.

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
