%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  jacobi
%global packver   3.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Jacobi Theta Functions and Related Functions

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 1.0.8
BuildRequires:    R-CRAN-Carlson 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-Rvcg 
Requires:         R-CRAN-Rcpp >= 1.0.8
Requires:         R-CRAN-Carlson 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-Rvcg 

%description
Evaluation of the Jacobi theta functions and related functions:
Weierstrass elliptic function, Weierstrass sigma function, Weierstrass
zeta function, Klein j-function, Dedekind eta function, lambda modular
function, Jacobi elliptic functions, Neville theta functions, Eisenstein
series, lemniscate elliptic functions, elliptic alpha function,
Rogers-Ramanujan continued fractions, and Dixon elliptic functions.
Complex values of the variable are supported.

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
