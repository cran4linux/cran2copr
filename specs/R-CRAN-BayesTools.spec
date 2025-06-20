%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BayesTools
%global packver   0.2.19
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.19
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for Bayesian Analyses

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-extraDistr 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-bridgesampling 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-extraDistr 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-bridgesampling 
Requires:         R-parallel 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-rlang 

%description
Provides tools for conducting Bayesian analyses and Bayesian model
averaging (Kass and Raftery, 1995, <doi:10.1080/01621459.1995.10476572>,
Hoeting et al., 1999, <doi:10.1214/ss/1009212519>). The package contains
functions for creating a wide range of prior distribution objects, mixing
posterior samples from 'JAGS' and 'Stan' models, plotting posterior
distributions, and etc... The tools for working with prior distribution
span from visualization, generating 'JAGS' and 'bridgesampling' syntax to
basic functions such as rng, quantile, and distribution functions.

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
