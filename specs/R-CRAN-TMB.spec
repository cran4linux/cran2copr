%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  TMB
%global packver   1.9.11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.9.11
Release:          1%{?dist}%{?buildtag}
Summary:          Template Model Builder: A General Random Effect Tool Inspired by 'ADMB'

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Recommends:       g++
BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-Matrix >= 1.0.12
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-Matrix >= 1.0.12
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 

%description
With this tool, a user should be able to quickly implement complex random
effect models through simple C++ templates. The package combines 'CppAD'
(C++ automatic differentiation), 'Eigen' (templated matrix-vector library)
and 'CHOLMOD' (sparse matrix routines available from R) to obtain an
efficient implementation of the applied Laplace approximation with exact
derivatives. Key features are: Automatic sparseness detection, parallelism
through 'BLAS' and parallel user templates.

%prep
%setup -q -c -n %{packname}
sed -ie '/onAttach/,+4d' %{packname}/R/zzz.R
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
