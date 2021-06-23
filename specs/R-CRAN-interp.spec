%global __brp_check_rpaths %{nil}
%global packname  interp
%global packver   1.0-33
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.33
Release:          3%{?dist}%{?buildtag}
Summary:          Interpolation Methods

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.12.9
BuildRequires:    R-CRAN-deldir 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-Rcpp >= 0.12.9
Requires:         R-CRAN-deldir 

%description
Bivariate data interpolation on regular and irregular grids, either linear
or using splines are the main part of this package.  It is intended to
provide FOSS replacement functions for the ACM licensed akima::interp and
tripack::tri.mesh functions. Currently the piecewise linear interpolation
part of akima::interp (and also akima::interpp) is implemented in
interp::interp, this corresponds to the call akima::interp(...,
linear=TRUE) which is the default setting and covers most of akima::interp
use cases in depending packages.  A re-implementation of Akimas spline
interpolation (akima::interp(..., linear=FALSE)) is currently under
development and will complete this package in a later version. Estimators
for partial derivatives are already available, these are a prerequisite
for the spline interpolation.  The basic part is currently a GPLed
triangulation algorithm (sweep hull algorithm by David Sinclair) providing
the starting point for the piecewise linear interpolator. As side effect
this algorithm is also used to provide replacements for the basic
functions of the tripack package which also suffer from the ACM
restrictions.  All functions are designed to be backward compatible with
their akima / tripack counterparts.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
