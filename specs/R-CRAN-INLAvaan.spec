%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  INLAvaan
%global packver   0.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.3
Release:          1%{?dist}%{?buildtag}
Summary:          Approximate Bayesian Latent Variable Analysis

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-blavaan 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-lavaan 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-modeest 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-qrng 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-statmod 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-ucminf 
BuildRequires:    R-utils 
Requires:         R-CRAN-blavaan 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-lavaan 
Requires:         R-methods 
Requires:         R-CRAN-modeest 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-qrng 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-statmod 
Requires:         R-stats 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-ucminf 
Requires:         R-utils 

%description
Implements approximate Bayesian inference for Structural Equation Models
(SEM) using a custom adaptation of the Integrated Nested Laplace
Approximation as described in Rue et al. (2009)
<doi:10.1111/j.1467-9868.2008.00700.x>. Provides a computationally
efficient alternative to Markov Chain Monte Carlo (MCMC) for Bayesian
estimation, allowing users to fit latent variable models using the
'lavaan' syntax.

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
