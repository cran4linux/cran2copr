%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sundials
%global packver   7.9.0-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          7.9.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Vendored 'SUNDIALS' Solver Suite for Linking by Other Packages

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core

%description
Bundles the pure-C part of the 'SUNDIALS' suite (CVODE, CVODES, ARKODE,
IDA, IDAS and KINSOL with the serial vector and the dense, band and
iterative linear solvers) and builds it into a static library. Other
packages use it by adding 'sundials' to 'LinkingTo' for the headers and
calling sundials::LdFlags() from their 'Makevars' to link the library. No
'Fortran', 'MPI', GPU or external third-party-library modules are
included. 'SUNDIALS' is described in Hindmarsh et al. (2005)
<doi:10.1145/1089014.1089020>.

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
