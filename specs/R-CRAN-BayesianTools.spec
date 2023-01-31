%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BayesianTools
%global packver   0.1.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.8
Release:          1%{?dist}%{?buildtag}
Summary:          General-Purpose MCMC and SMC Samplers and Tools for Bayesian Statistics

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.2
Requires:         R-core >= 3.1.2
BuildRequires:    R-CRAN-Rcpp >= 0.12.12
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-emulator 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-tmvtnorm 
BuildRequires:    R-CRAN-IDPmisc 
BuildRequires:    R-CRAN-ellipse 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-msm 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-DHARMa 
BuildRequires:    R-CRAN-gap 
BuildRequires:    R-CRAN-bridgesampling 
Requires:         R-CRAN-Rcpp >= 0.12.12
Requires:         R-CRAN-coda 
Requires:         R-CRAN-emulator 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-tmvtnorm 
Requires:         R-CRAN-IDPmisc 
Requires:         R-CRAN-ellipse 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-msm 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-Matrix 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-CRAN-DHARMa 
Requires:         R-CRAN-gap 
Requires:         R-CRAN-bridgesampling 

%description
General-purpose MCMC and SMC samplers, as well as plot and diagnostic
functions for Bayesian statistics, with a particular focus on calibrating
complex system models. Implemented samplers include various Metropolis
MCMC variants (including adaptive and/or delayed rejection MH), the
T-walk, two differential evolution MCMCs, two DREAM MCMCs, and a
sequential Monte Carlo (SMC) particle filter.

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
