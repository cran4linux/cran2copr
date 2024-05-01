%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ratioOfQsprays
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Fractions of Multivariate Polynomials with Rational Coefficients

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-qspray >= 3.0.0
BuildRequires:    R-CRAN-gmp 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-Ryacas 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-BH 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-RcppCGAL 
Requires:         R-CRAN-qspray >= 3.0.0
Requires:         R-CRAN-gmp 
Requires:         R-methods 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-Ryacas 
Requires:         R-utils 

%description
Based on the 'qspray' package, this package introduces the new type
'ratioOfQsprays'. An object of type 'qspray' represents a multivariate
polynomial with rational coefficients while an object of type
'ratioOfQsprays', defined by two 'qspray' objects, represents a fraction
of two multivariate polynomials with rational coefficients. Arithmetic
operations for these objects are available, and they always return
irreducible fractions. Other features include: differentiation,
evaluation, conversion to a function, and fine control of the way to print
a 'ratioOfQsprays' object. The 'C++' library 'CGAL' is used to make the
fractions irreducible.

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
