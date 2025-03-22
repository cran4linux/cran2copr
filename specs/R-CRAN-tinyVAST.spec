%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tinyVAST
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Multivariate Spatio-Temporal Models using Structural Equations

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-TMB >= 1.9.17
BuildRequires:    R-CRAN-Matrix >= 1.3.0
BuildRequires:    R-CRAN-corpcor 
BuildRequires:    R-CRAN-fmesher 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-sem 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-sfnetworks 
BuildRequires:    R-CRAN-units 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-sdmTMB 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-TMB >= 1.9.17
Requires:         R-CRAN-Matrix >= 1.3.0
Requires:         R-CRAN-corpcor 
Requires:         R-CRAN-fmesher 
Requires:         R-CRAN-igraph 
Requires:         R-methods 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-sem 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-sfnetworks 
Requires:         R-CRAN-units 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-sdmTMB 

%description
Fits a wide variety of multivariate spatio-temporal models with
simultaneous and lagged interactions among variables (including vector
autoregressive spatio-temporal ('VAST') dynamics) for areal, continuous,
or network spatial domains. It includes time-variable, space-variable, and
space-time-variable interactions using dynamic structural equation models
('DSEM') as expressive interface, and the 'mgcv' package to specify
splines via the formula interface.  See Thorson et al. (2024)
<doi:10.48550/arXiv.2401.10193> for more details.

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
