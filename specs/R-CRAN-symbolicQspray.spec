%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  symbolicQspray
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Multivariate Polynomials with Symbolic Parameters in their Coefficients

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-qspray >= 3.0.0
BuildRequires:    R-CRAN-ratioOfQsprays 
BuildRequires:    R-CRAN-gmp 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-BH 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-RcppCGAL 
Requires:         R-CRAN-qspray >= 3.0.0
Requires:         R-CRAN-ratioOfQsprays 
Requires:         R-CRAN-gmp 
Requires:         R-methods 
Requires:         R-CRAN-Rcpp 
Requires:         R-utils 

%description
Introduces the 'symbolicQspray' objects. Such an object represents a
multivariate polynomial whose coefficients are fractions of multivariate
polynomials with rational coefficients. The package allows arithmetic on
such polynomials. It is based on the 'qspray' and 'ratioOfQsprays'
packages. Some functions for 'qspray' polynomials have their counterpart
for 'symbolicQspray' polynomials. A 'symbolicQspray' polynomial should not
be seen as a polynomial on the field of fractions of rational polynomials,
but should rather be seen as a polynomial with rational coefficients
depending on some parameters, symbolically represented, with a dependence
given by fractions of rational polynomials.

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
