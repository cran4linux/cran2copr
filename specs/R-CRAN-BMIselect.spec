%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BMIselect
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian MI-LASSO for Variable Selection on Multiply-Imputed Datasets

License:          Apache License (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MCMCpack 
BuildRequires:    R-CRAN-mvnfast 
BuildRequires:    R-CRAN-GIGrvg 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-Rfast 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-arm 
BuildRequires:    R-CRAN-mice 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-posterior 
Requires:         R-CRAN-MCMCpack 
Requires:         R-CRAN-mvnfast 
Requires:         R-CRAN-GIGrvg 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-Rfast 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-arm 
Requires:         R-CRAN-mice 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-stringr 
Requires:         R-stats 
Requires:         R-CRAN-posterior 

%description
Provides a suite of Bayesian MI-LASSO for variable selection methods for
multiply-imputed datasets. The package includes four Bayesian MI-LASSO
models using shrinkage (Multi-Laplace, Horseshoe, ARD) and Spike-and-Slab
(Spike-and-Laplace) priors, along with tools for model fitting via MCMC,
four-step projection predictive variable selection, and hyperparameter
calibration. Methods are suitable for both continuous and binary
covariates under missing-at-random assumptions. See Zou, J., Wang, S. and
Chen, Q. (2025), Bayesian MI-LASSO for Variable Selection on
Multiply-Imputed Data. ArXiv, 2211.00114. <doi:10.48550/arXiv.2211.00114>
for more details. We also provide the frequentist`s MI-LASSO function.

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
