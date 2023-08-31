%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  footBayes
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Fitting Bayesian and MLE Football Models

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Recommends:       pandoc
BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rstan >= 2.18.1
BuildRequires:    R-CRAN-arm 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-bayesplot 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-extraDistr 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-metRology 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-tidyverse 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-rstantools
Requires:         R-CRAN-rstan >= 2.18.1
Requires:         R-CRAN-arm 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-bayesplot 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-extraDistr 
Requires:         R-parallel 
Requires:         R-CRAN-metRology 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-tidyverse 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-rstantools

%description
This is the first package allowing for the estimation, visualization and
prediction of the most well-known football models: double Poisson,
bivariate Poisson, Skellam, student_t, diagonal-inflated bivariate
Poisson, and zero-inflated Skellam. The package allows Hamiltonian Monte
Carlo (HMC) estimation through the underlying Stan environment and Maximum
Likelihood estimation (MLE, for 'static' models only). The model
construction relies on the most well-known football references, such as
Dixon and Coles (1997) <doi:10.1111/1467-9876.00065>, Karlis and Ntzoufras
(2003) <doi:10.1111/1467-9884.00366> and Egidi, Pauli and Torelli (2018)
<doi:10.1177/1471082X18798414>.

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
