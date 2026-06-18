%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Uno
%global packver   2.7.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.7.4
Release:          1%{?dist}%{?buildtag}
Summary:          R Interface to the 'Uno' Nonlinear Optimization Solver

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-rmumps >= 5.2.1.41
BuildRequires:    R-CRAN-cpp11 
Requires:         R-CRAN-rmumps >= 5.2.1.41

%description
Bindings to 'Uno' (Unifying Nonlinear Optimization), a C++ solver for
smooth nonlinearly constrained optimization. 'Uno' unifies Lagrange-Newton
methods, including sequential quadratic programming and interior-point
methods, by decomposing them into interacting building blocks
(constraint-relaxation, inequality-handling, Hessian, and globalization
strategies) that can be freely combined, either through options or through
presets that reproduce established solvers such as 'filterSQP' and
'IPOPT'. The framework is described in Vanaret and Leyffer (2024)
<doi:10.48550/arXiv.2406.13454>.

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
