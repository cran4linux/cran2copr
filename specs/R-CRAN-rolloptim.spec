%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rolloptim
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Rolling Optimizations

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppParallel 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-RcppParallel 

%description
Analytical computation of rolling optimization for time-series data. The
'rolloptim' package solves constrained quadratic and linear programs in
closed form by applying Lagrangian multipliers and the Karush-Kuhn-Tucker
conditions (Kuhn and Tucker, 1951, <doi:10.1525/9780520411586-036>) to
perform mean-variance portfolio optimization (Markowitz, 1952,
<doi:10.1111/j.1540-6261.1952.tb01525.x>) over rolling windows. For each
window, the analytical solution computes the optimal weights that minimize
variance, maximize expected return, minimize residual sum of squares, or
maximize quadratic utility, subject to a total-weight equality constraint
and box bounds on each weight. Use cases include mean-variance portfolio
optimization, expected-return maximization, and constrained regression.
The package supports rolling optimizations with constraints via the total,
lower, and upper arguments. The implementation accepts rolling moments
computed via the 'roll' package and uses 'RcppArmadillo' for linear
algebra, with parallelism across windows provided by 'RcppParallel'.

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
