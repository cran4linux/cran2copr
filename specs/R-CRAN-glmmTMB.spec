%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  glmmTMB
%global packver   1.1.11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.11
Release:          1%{?dist}%{?buildtag}
Summary:          Generalized Linear Mixed Models using Template Model Builder

License:          AGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildRequires:    R-CRAN-TMB >= 1.9.0
BuildRequires:    R-CRAN-lme4 >= 1.1.18.9000
BuildRequires:    R-CRAN-reformulas >= 0.2.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-TMB >= 1.9.0
Requires:         R-CRAN-lme4 >= 1.1.18.9000
Requires:         R-CRAN-reformulas >= 0.2.0
Requires:         R-methods 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-mgcv 

%description
Fit linear and generalized linear mixed models with various extensions,
including zero-inflation. The models are fitted using maximum likelihood
estimation via 'TMB' (Template Model Builder). Random effects are assumed
to be Gaussian on the scale of the linear predictor and are integrated out
using the Laplace approximation. Gradients are calculated using automatic
differentiation.

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
