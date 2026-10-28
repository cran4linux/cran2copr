%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RcppTrust
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Thread-Safe C++ Trust Region Optimizers

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-Rcpp 

%description
Thread-safe C++ trust region optimizers, each exposed both as an R
function and as a C-callable entry point (with function pointers
registered for other packages to call without linking against this
package's shared library) so they can be used from parallel C++ code such
as in 'nlmixr2est'. Includes a port of the two-derivative trust region
algorithm in the 'trust' package by Charles J. Geyer; a port of the
Steihaug truncated conjugate-gradient trust region method from the 'basin'
Rust crate (Steihaug (1983) <doi:10.1137/0720042>); and ports of M. J. D.
Powell's derivative-free BOBYQA (Powell (2009), Report DAMTP 2009/NA06)
and NEWUOA (Powell (2006) <doi:10.1007/0-387-30065-1_16>) Fortran 77 code
<https://github.com/libprima/prima/tree/main/fortran/original>, as
modified and distributed in the 'minqa' package, whose R interface is
reproduced.

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
