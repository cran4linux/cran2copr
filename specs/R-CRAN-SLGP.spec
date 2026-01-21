%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SLGP
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Spatial Logistic Gaussian Process for Field Density Estimation

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-RcppParallel >= 5.0.1
BuildRequires:    R-CRAN-StanHeaders >= 2.21.0
BuildRequires:    R-CRAN-rstan >= 2.18.1
BuildRequires:    R-CRAN-BH >= 1.66.0
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.3.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.0
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-DiceDesign 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-mvnfast 
BuildRequires:    R-CRAN-GoFKernel 
BuildRequires:    R-CRAN-rstantools 
BuildRequires:    R-CRAN-rstantools
Requires:         R-CRAN-RcppParallel >= 5.0.1
Requires:         R-CRAN-rstan >= 2.18.1
Requires:         R-CRAN-Rcpp >= 0.12.0
Requires:         R-stats 
Requires:         R-CRAN-DiceDesign 
Requires:         R-methods 
Requires:         R-CRAN-mvnfast 
Requires:         R-CRAN-GoFKernel 
Requires:         R-CRAN-rstantools 
Requires:         R-CRAN-rstantools

%description
Provides tools for conditional and spatially dependent density estimation
using Spatial Logistic Gaussian Processes (SLGPs). The approach represents
probability densities through finite-rank Gaussian process priors
transformed via a spatial logistic density transformation, enabling
flexible non-parametric modeling of heterogeneous data. Functionality
includes density prediction, quantile and moment estimation, sampling
methods, and preprocessing routines for basis functions. Applications
arise in spatial statistics, machine learning, and uncertainty
quantification. The methodology builds on the framework of Leonard (1978)
<doi:10.1111/j.2517-6161.1978.tb01655.x>, Lenk (1988)
<doi:10.1080/01621459.1988.10478625>, Tokdar (2007)
<doi:10.1198/106186007X210206>, Tokdar (2010) <doi:10.1214/10-BA605>, and
is further aligned with recent developments in Bayesian non-parametric
modelling: see Gautier (2023) <https://boristheses.unibe.ch/4377/>, and
Gautier (2025) <doi:10.48550/arXiv.2110.02876>).

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
