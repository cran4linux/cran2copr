%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BSTFA
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Spatio-Temporal Factor Analysis Model

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-MCMCpack 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-npreg 
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-CRAN-scatterplot3d 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-MCMCpack 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-npreg 
Requires:         R-CRAN-matrixcalc 
Requires:         R-CRAN-scatterplot3d 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-Matrix 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-CRAN-RcppArmadillo 

%description
Implements Bayesian spatio-temporal factor analysis models for
multivariate data observed across space and time. The package provides
tools for model fitting via Markov chain Monte Carlo (MCMC), spatial and
temporal interpolation, and visualization of latent factors and loadings
to support inference and exploration of underlying spatio-temporal
patterns. Designed for use in environmental, ecological, or public health
applications, with support for posterior prediction and uncertainty
quantification. Includes functions such as BSTFA() for model fitting and
plot_factor() to visualize the latent processes.  Functions are based on
and extended from methods described in Berrett, et al. (2020)
<doi:10.1002/env.2609>.

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
