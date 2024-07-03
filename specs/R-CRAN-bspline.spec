%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bspline
%global packver   2.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          B-Spline Interpolation and Regression

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 1.0.7
BuildRequires:    R-CRAN-nlsic >= 1.0.2
BuildRequires:    R-CRAN-arrApply 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 1.0.7
Requires:         R-CRAN-nlsic >= 1.0.2
Requires:         R-CRAN-arrApply 

%description
Build and use B-splines for interpolation and regression. In case of
regression, equality constraints as well as monotonicity and/or positivity
of B-spline weights can be imposed. Moreover, knot positions (not only
spline weights) can be part of optimized parameters too. For this end,
'bspline' is able to calculate Jacobian of basis vectors as function of
knot positions. User is provided with functions calculating spline values
at arbitrary points. These functions can be differentiated and integrated
to obtain B-splines calculating derivatives/integrals at any point.
B-splines of this package can simultaneously operate on a series of curves
sharing the same set of knots. 'bspline' is written with concern about
computing performance that's why the basis and Jacobian calculation is
implemented in C++. The rest is implemented in R but without notable
impact on computing speed.

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
