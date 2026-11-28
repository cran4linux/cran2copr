%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ceres
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          An Interface to 'Ceres Solver' for Non-Linear Least Squares and Optimization

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-Rcpp 
Requires:         R-stats 

%description
Provides an interface to the 'Ceres Solver' C++ library
<https://github.com/ceres-solver/ceres-solver>. 'Ceres Solver' is an open
source library for modeling and solving large, complicated optimization
problems. It can solve non-linear least squares problems with bounds
constraints and general unconstrained optimization problems. It is a
mature, feature rich and high-performance library that has been used in
production at Google since 2010. Non-linear least squares problems with
residuals written in R can be solved with ceres_nls(), with optional
bounds and robust loss functions. The bundled library is built from source
and can also be used from C++ through 'Rcpp', either with
Rcpp::sourceCpp() or from other packages.

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
