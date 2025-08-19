%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dynemu
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Emulation of Dynamic Simulators via One-Step-Ahead Approach

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-deSolve 
BuildRequires:    R-CRAN-plgp 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-MASS 
Requires:         R-CRAN-deSolve 
Requires:         R-CRAN-plgp 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-MASS 

%description
Performs emulation of dynamic simulators using Gaussian process via
one-step ahead approach. The package implements a flexible framework for
approximating time-dependent outputs from computationally expensive
dynamic systems. It is specifically designed for nonlinear dynamic systems
where full simulations may be costly. The underlying Gaussian process
model accounts for temporal dependency through the one-step-ahead
formulation, allowing for accurate emulation of complex dynamics.
Hyperparameters are estimated via maximum likelihood. For methodological
details, see Heo (2025, <doi:10.48550/arXiv.2503.20250>) for exact method,
and Mohammadi, Challenor, and Goodfellow (2019,
<doi:10.1016/j.csda.2019.05.006>) for Monte Carlo method.

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
