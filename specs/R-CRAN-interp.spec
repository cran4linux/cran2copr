%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  interp
%global packver   1.1-6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.6
Release:          1%{?dist}%{?buildtag}
Summary:          Interpolation Methods

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.9
BuildRequires:    R-CRAN-deldir 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-Rcpp >= 0.12.9
Requires:         R-CRAN-deldir 

%description
Bivariate data interpolation on regular and irregular grids, either linear
or using splines are the main part of this package.  It is intended to
provide FOSS replacement functions for the ACM licensed akima::interp and
tripack::tri.mesh functions. Linear interpolation is implemented in
interp::interp(..., method="linear"), this corresponds to the call
akima::interp(..., linear=TRUE) which is the default setting and covers
most of akima::interp use cases in depending packages. A re-implementation
of Akimas irregular grid spline interpolation (akima::interp(...,
linear=FALSE)) is now also available via interp::interp(...,
method="akima"). Estimators for partial derivatives are now also available
in interp::locpoly(), these are a prerequisite for the spline
interpolation. The basic part is a GPLed triangulation algorithm (sweep
hull algorithm by David Sinclair) providing the starting point for the
irregular grid interpolator. As side effect this algorithm is also used to
provide replacements for almost all functions of the tripack package which
also suffers from the same ACM license restrictions. All functions are
designed to be backward compatible with their akima / tripack
counterparts.

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
