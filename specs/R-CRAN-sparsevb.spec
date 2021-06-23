%global __brp_check_rpaths %{nil}
%global packname  sparsevb
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Spike-and-Slab Variational Bayes for Linear and Logistic Regression

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-glmnet >= 4.0
BuildRequires:    R-CRAN-selectiveInference >= 1.2.5
BuildRequires:    R-CRAN-Rcpp >= 1.0.5
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-RcppEnsmallen 
Requires:         R-CRAN-glmnet >= 4.0
Requires:         R-CRAN-selectiveInference >= 1.2.5
Requires:         R-CRAN-Rcpp >= 1.0.5
Requires:         R-stats 

%description
Implements variational Bayesian algorithms to perform scalable variable
selection for sparse, high-dimensional linear and logistic regression
models. Features include a novel prioritized updating scheme, which uses a
preliminary estimator of the variational means during initialization to
generate an updating order prioritizing large, more relevant,
coefficients. Sparsity is induced via spike-and-slab priors with either
Laplace or Gaussian slabs. By default, the heavier-tailed Laplace density
is used. Formal derivations of the algorithms and asymptotic consistency
results may be found in Kolyan Ray and Botond Szabo (2020)
<doi:10.1080/01621459.2020.1847121> and Kolyan Ray, Botond Szabo, and
Gabriel Clara (2020) <arXiv:2010.11665>.

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
