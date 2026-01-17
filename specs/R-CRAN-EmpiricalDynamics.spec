%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  EmpiricalDynamics
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Empirical Discovery of Differential Equations from Time Series Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-gridExtra >= 2.3
BuildRequires:    R-CRAN-minpack.lm >= 1.2
BuildRequires:    R-CRAN-CVXR >= 1.0
BuildRequires:    R-CRAN-lmtest >= 0.9
BuildRequires:    R-CRAN-signal >= 0.7
BuildRequires:    R-CRAN-JuliaCall >= 0.17
BuildRequires:    R-CRAN-tseries >= 0.10
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
BuildRequires:    R-methods 
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-gridExtra >= 2.3
Requires:         R-CRAN-minpack.lm >= 1.2
Requires:         R-CRAN-CVXR >= 1.0
Requires:         R-CRAN-lmtest >= 0.9
Requires:         R-CRAN-signal >= 0.7
Requires:         R-CRAN-JuliaCall >= 0.17
Requires:         R-CRAN-tseries >= 0.10
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-utils 
Requires:         R-methods 

%description
A comprehensive toolkit for discovering differential and difference
equations from empirical time series data using symbolic regression. The
package implements a complete workflow from data preprocessing (including
Total Variation Regularized differentiation for noisy economic data),
visual exploration of dynamical structure, and symbolic equation discovery
via genetic algorithms. It leverages a high-performance 'Julia' backend
('SymbolicRegression.jl') to provide industrial-grade robustness,
physics-informed constraints, and rigorous out-of-sample validation.
Designed for economists, physicists, and researchers studying dynamical
systems from observational data.

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
