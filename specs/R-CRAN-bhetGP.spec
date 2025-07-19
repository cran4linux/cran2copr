%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bhetGP
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Heteroskedastic Gaussian Processes

License:          LGPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-GpGp 
BuildRequires:    R-CRAN-GPvecchia 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-FNN 
BuildRequires:    R-CRAN-hetGP 
BuildRequires:    R-CRAN-laGP 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-parallel 
Requires:         R-CRAN-GpGp 
Requires:         R-CRAN-GPvecchia 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-FNN 
Requires:         R-CRAN-hetGP 
Requires:         R-CRAN-laGP 

%description
Performs Bayesian posterior inference for heteroskedastic Gaussian
processes. Models are trained through MCMC including elliptical slice
sampling (ESS) of latent noise processes and Metropolis-Hastings sampling
of kernel hyperparameters. Replicates are handled efficientyly through a
Woodbury formulation of the joint likelihood for the mean and noise
process (Binois, M., Gramacy, R., Ludkovski, M. (2018)
<doi:10.1080/10618600.2018.1458625>) For large data, Vecchia-approximation
for faster computation is leveraged (Sauer, A., Cooper, A., and Gramacy,
R., (2023), <doi:10.1080/10618600.2022.2129662>). Incorporates 'OpenMP'
and SNOW parallelization and utilizes 'C'/'C++' under the hood.

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
