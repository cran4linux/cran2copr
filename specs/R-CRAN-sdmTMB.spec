%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sdmTMB
%global packver   0.7.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.2
Release:          1%{?dist}%{?buildtag}
Summary:          Spatial and Spatiotemporal SPDE-Based GLMMs with 'TMB'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-TMB >= 1.8.0
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-fmesher 
BuildRequires:    R-CRAN-fishMod 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-TMB >= 1.8.0
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-fmesher 
Requires:         R-CRAN-fishMod 
Requires:         R-CRAN-generics 
Requires:         R-graphics 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-Matrix 
Requires:         R-methods 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-rlang 
Requires:         R-stats 

%description
Implements spatial and spatiotemporal GLMMs (Generalized Linear Mixed
Effect Models) using 'TMB', 'fmesher', and the SPDE (Stochastic Partial
Differential Equation) Gaussian Markov random field approximation to
Gaussian random fields. One common application is for spatially explicit
species distribution models (SDMs). See Anderson et al. (2024)
<doi:10.1101/2022.03.24.485545>.

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
