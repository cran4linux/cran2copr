%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  limSolve
%global packver   1.5.7.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.7.1
Release:          1%{?dist}%{?buildtag}
Summary:          Solving Linear Inverse Models

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-CRAN-lpSolve 
BuildRequires:    R-CRAN-MASS 
Requires:         R-CRAN-quadprog 
Requires:         R-CRAN-lpSolve 
Requires:         R-CRAN-MASS 

%description
Functions that (1) find the minimum/maximum of a linear or quadratic
function: min or max (f(x)), where f(x) = ||Ax-b||^2 or f(x) =
sum(a_i*x_i) subject to equality constraints Ex=f and/or inequality
constraints Gx>=h, (2) sample an underdetermined- or overdetermined system
Ex=f subject to Gx>=h, and if applicable Ax~=b, (3) solve a linear system
Ax=B for the unknown x. It includes banded and tridiagonal linear systems.

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
