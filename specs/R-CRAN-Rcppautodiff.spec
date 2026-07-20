%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Rcppautodiff
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          An Interface to the C++ Automatic Differentiation Library 'autodiff'

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 1.0.8.3
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-Rcpp >= 1.0.8.3
Requires:         R-CRAN-RcppEigen 

%description
Provides an interface from R to the 'autodiff' library
<https://autodiff.github.io/>, a modern header-only C++ library for
automatic differentiation. Unlike numerical differentiation, automatic
differentiation computes derivatives of functions to machine precision
without truncation error, using either forward or reverse mode. The
'autodiff' header files are shipped with this package so that other R
packages can use them by including 'Rcppautodiff' in the 'LinkingTo' field
of their 'DESCRIPTION' file. Example programs demonstrate computing
derivatives of single-variable and multi-variable functions, gradient
vectors, Jacobian matrices and derivatives with respect to parameters,
using 'Rcpp' and 'RcppEigen'.

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
