%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  qspray
%global packver   3.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Multivariate Polynomials with Rational Coefficients

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    gmp-devel
BuildRequires:    mpfr-devel
BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 1.0.9
BuildRequires:    R-CRAN-DescTools 
BuildRequires:    R-CRAN-gmp 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-partitions 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-RationalMatrix 
BuildRequires:    R-CRAN-Ryacas 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-Rcpp >= 1.0.9
Requires:         R-CRAN-DescTools 
Requires:         R-CRAN-gmp 
Requires:         R-methods 
Requires:         R-CRAN-partitions 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-RationalMatrix 
Requires:         R-CRAN-Ryacas 
Requires:         R-utils 

%description
Symbolic calculation and evaluation of multivariate polynomials with
rational coefficients. This package is strongly inspired by the 'spray'
package. It provides a function to compute Gröbner bases (reference
<doi:10.1007/978-3-319-16721-3>). It also includes some features for
symmetric polynomials, such as the Hall inner product. The header file of
the C++ code can be used by other packages. It provides the templated
class 'Qspray' that can be used to represent and to deal with multivariate
polynomials with another type of coefficients.

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
