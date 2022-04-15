%global __brp_check_rpaths %{nil}
%global packname  deSolve
%global packver   1.32
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.32
Release:          1%{?dist}%{?buildtag}
Summary:          Solvers for Initial Value Problems of Differential Equations ('ODE', 'DAE', 'DDE')

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-methods 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
Requires:         R-methods 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-stats 

%description
Functions that solve initial value problems of a system of first-order
ordinary differential equations ('ODE'), of partial differential equations
('PDE'), of differential algebraic equations ('DAE'), and of delay
differential equations.  The functions provide an interface to the FORTRAN
functions 'lsoda', 'lsodar', 'lsode', 'lsodes' of the 'ODEPACK'
collection, to the FORTRAN functions 'dvode', 'zvode' and 'daspk' and a
C-implementation of solvers of the 'Runge-Kutta' family with fixed or
variable time steps.  The package contains routines designed for solving
'ODEs' resulting from 1-D, 2-D and 3-D partial differential equations
('PDE') that have been converted to 'ODEs' by numerical differencing.

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
