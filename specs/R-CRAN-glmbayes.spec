%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  glmbayes
%global packver   0.9.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.7
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Generalized Linear Models (IID Samples)

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 1.1.1
BuildRequires:    R-CRAN-opencltools >= 0.8.1
BuildRequires:    R-CRAN-Rdpack >= 0.11.0
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-insight 
BuildRequires:    R-CRAN-bayestestR 
BuildRequires:    R-CRAN-RcppParallel 
BuildRequires:    R-CRAN-nmathopencl 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 1.1.1
Requires:         R-CRAN-opencltools >= 0.8.1
Requires:         R-CRAN-Rdpack >= 0.11.0
Requires:         R-CRAN-MASS 
Requires:         R-stats 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-insight 
Requires:         R-CRAN-bayestestR 
Requires:         R-CRAN-RcppParallel 
Requires:         R-CRAN-nmathopencl 

%description
Provides Bayesian linear and generalized linear model fitting with
independent and identically distributed (iid) posterior samples. The main
functions mirror R's lm() and glm() interfaces while adding prior family
specifications for Gaussian, Poisson, binomial, and Gamma models with
log-concave likelihoods. Sampling for supported non-conjugate models uses
accept-reject methods based on likelihood subgradients as in Nygren and
Nygren (2006) <doi:10.1198/016214506000000357>. The package also includes
tools for prior setup, posterior summaries, prediction, diagnostics,
simulation, vignettes, and optional 'OpenCL' acceleration for larger
models.

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
