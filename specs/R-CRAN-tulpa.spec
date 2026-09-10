%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tulpa
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Template Unified Latent Process Architecture for Bayesian Hierarchical Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.12
BuildRequires:    R-CRAN-tulpaMesh >= 0.1.3
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-stats 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
BuildRequires:    R-methods 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-Rcpp >= 1.0.12
Requires:         R-CRAN-tulpaMesh >= 0.1.3
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-generics 
Requires:         R-CRAN-lifecycle 
Requires:         R-stats 
Requires:         R-tools 
Requires:         R-utils 
Requires:         R-methods 
Requires:         R-graphics 
Requires:         R-grDevices 

%description
A general-purpose engine for fitting Bayesian hierarchical models with
spatial fields, temporal effects, spatially varying coefficients, and
multiple inference backends. Scalable spatial structure includes Hilbert
space approximate Gaussian processes (HSGP; Riutort-Mayol et al. 2023
<doi:10.1007/s11222-022-10167-2>), nearest-neighbor Gaussian processes
(NNGP; Datta et al. 2016 <doi:10.1080/01621459.2015.1044091>), intrinsic
conditional autoregressive models (ICAR; Besag, York, and Mollie 1991
<doi:10.1007/BF00116466>), the reparameterized Besag-York-Mollie model
(BYM2; Riebler et al. 2016 <doi:10.1177/0962280216660421>), and stochastic
partial differential equation fields (SPDE; Lindgren, Rue, and Lindstrom
2011 <doi:10.1111/j.1467-9868.2011.00777.x>). Temporal structure covers
random walks, autoregressive processes, and Gaussian processes. Inference
is tiered by correctness guarantee: exact Hamiltonian Monte Carlo with the
No-U-Turn sampler, Laplace and nested Laplace approximations with
hyperparameter integration (Rue, Martino, and Chopin 2009
<doi:10.1111/j.1467-9868.2008.00700.x>), and variational inference.
Model-specific packages plug observation likelihoods into the engine
through a templated C++ callback interface.

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
