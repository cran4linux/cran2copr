%global __brp_check_rpaths %{nil}
%global packname  spikeSlabGAM
%global packver   1.1-19
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.19
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Variable Selection and Model Choice for Generalized Additive Mixed Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.1
Requires:         R-core >= 2.15.1
BuildRequires:    R-CRAN-ggplot2 >= 2.0.0
BuildRequires:    R-CRAN-gridExtra >= 2.0
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-interp 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-MCMCpack 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-R2WinBUGS 
BuildRequires:    R-CRAN-reshape 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-splines 
BuildRequires:    R-parallel 
Requires:         R-CRAN-ggplot2 >= 2.0.0
Requires:         R-CRAN-gridExtra >= 2.0
Requires:         R-CRAN-coda 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-interp 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-MCMCpack 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-R2WinBUGS 
Requires:         R-CRAN-reshape 
Requires:         R-CRAN-scales 
Requires:         R-splines 
Requires:         R-parallel 

%description
Bayesian variable selection, model choice, and regularized estimation for
(spatial) generalized additive mixed regression models via stochastic
search variable selection with spike-and-slab priors.

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
