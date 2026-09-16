%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sTiles
%global packver   2026.9.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2026.9.4
Release:          1%{?dist}%{?buildtag}
Summary:          Tile-Based Sparse Cholesky Factorization and Selected Inverse

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-methods 
Requires:         R-CRAN-Matrix 
Requires:         R-tools 
Requires:         R-utils 

%description
Interface to the 'sTiles' framework for tile-based sparse Cholesky
factorization: log-determinants, selected inverse (marginal variances) and
triangular solves, with symbolic reuse so that repeated factorization of
matrices sharing one sparsity pattern pays the ordering cost only once, as
in a hyperparameter sweep. The compiled glue in this package resolves its
symbols at run time against the 'sTiles' solver library ('libstiles'),
which is a separate component distributed under its own terms and is not
part of this package. Install it once with 'sTiles_install_library()', or
point the package at a copy you already have with the 'STILES_LIB'
environment variable.

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
