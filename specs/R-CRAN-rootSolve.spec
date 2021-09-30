%global __brp_check_rpaths %{nil}
%global packname  rootSolve
%global packver   1.8.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.8.2.3
Release:          1%{?dist}%{?buildtag}
Summary:          Nonlinear Root Finding, Equilibrium and Steady-State Analysis of Ordinary Differential Equations

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.01
Requires:         R-core >= 2.01
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 

%description
Routines to find the root of nonlinear functions, and to perform
steady-state and equilibrium analysis of ordinary differential equations
(ODE). Includes routines that: (1) generate gradient and jacobian matrices
(full and banded), (2) find roots of non-linear equations by the
'Newton-Raphson' method, (3) estimate steady-state conditions of a system
of (differential) equations in full, banded or sparse form, using the
'Newton-Raphson' method, or by dynamically running, (4) solve the
steady-state conditions for uni-and multicomponent 1-D, 2-D, and 3-D
partial differential equations, that have been converted to ordinary
differential equations by numerical differencing (using the
method-of-lines approach). Includes fortran code.

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
test $(gcc -dumpversion) -ge 10 && mkdir -p ~/.R && echo "FFLAGS=$(R CMD config FFLAGS) -fallow-argument-mismatch" > ~/.R/Makevars
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
