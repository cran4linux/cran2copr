%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SpatialGEV
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Fit Spatial Generalized Extreme Value Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-TMB >= 1.7.16
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-evd 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-TMB >= 1.7.16
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-evd 
Requires:         R-stats 
Requires:         R-CRAN-Matrix 
Requires:         R-methods 

%description
Fit latent variable models with the GEV distribution as the data
likelihood and the GEV parameters following latent Gaussian processes. The
models in this package are built using the template model builder 'TMB' in
R, which has the fast ability to integrate out the latent variables using
Laplace approximation. This package allows the users to choose in the fit
function which GEV parameter(s) is considered as a spatially varying
random effect following a Gaussian process, so the users can fit spatial
GEV models with different complexities to their dataset without having to
write the models in 'TMB' by themselves. This package also offers methods
to sample from both fixed and random effects posteriors as well as the
posterior predictive distributions at different spatial locations. Methods
for fitting this class of models are described in Chen, Ramezan, and Lysy
(2024) <doi:10.48550/arXiv.2110.07051>.

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
