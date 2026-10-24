%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  margEVT
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          1%{?dist}%{?buildtag}
Summary:          Regularized Point Processes and Stochastic Marginalization for Extremes

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-utils 

%description
Implements a non-stationary extreme value analysis framework by coupling a
covariate-driven non-homogeneous Poisson process (NHPP) with (adaptive)
elastic-net regularization, analytical gradients and a lower bound on the
shape parameter. Provides methods for estimating conditional return levels
and unconditional (marginalized) return levels via parametric stochastic
integration over stable vector autoregressive VAR(p) covariate
trajectories, or non-parametric annual-block resampling. Supports
block-specific penalty controls, BIC selection along a regularization
path, Karush-Kuhn-Tucker convergence checks, time-rescaling residual
diagnostics, conditional parametric bootstrap inference, and walk-forward
assessment.

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
