%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DIFM
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Dynamic ICAR Spatiotemporal Factor Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-Rcpp >= 1.0.10
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-LaplacesDemon 
BuildRequires:    R-CRAN-spdep 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 1.0.10
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-LaplacesDemon 
Requires:         R-CRAN-spdep 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-sp 

%description
Bayesian factor models are effective tools for dimension reduction. This
is especially applicable to multivariate large-scale datasets. It allows
researchers to understand the latent factors of the data which are the
linear or non-linear combination of the variables. Dynamic Intrinsic
Conditional Autocorrelative Priors (ICAR) Spatiotemporal Factor Models
'DIFM' package provides function to run Markov Chain Monte Carlo (MCMC),
evaluation methods and visual plots from Shin and Ferreira
(2023)<doi:10.1016/j.spasta.2023.100763>. Our method is a class of
Bayesian factor model which can account for spatial and temporal
correlations. By incorporating these correlations, the model can capture
specific behaviors and provide predictions.

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
