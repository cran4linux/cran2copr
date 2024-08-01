%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  resultant
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Utilities for Multivariate Polynomials with Rational Coefficients

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-qspray >= 3.1.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-gmp 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-BH 
BuildRequires:    R-CRAN-RcppCGAL 
Requires:         R-CRAN-qspray >= 3.1.0
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-gmp 
Requires:         R-utils 

%description
Computation of resultant, subresultants, greatest common divisor, integral
division (aka division without remainder) of two multivariate polynomials
with rational coefficients, Sturm-Habicht sequence and square-free
factorization of a multivariate polynomial with rational coefficients. The
computations are performed by the 'C++' library 'CGAL'
(<https://www.cgal.org/>). Resultants have applications in polynomial
systems solving, number theory, and algebraic geometry. The package also
contains some functions computing the number of real roots of a univariate
polynomial with rational coefficients, and a function computing the
division with remainder of two univariate polynomials with rational
coefficients.

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
