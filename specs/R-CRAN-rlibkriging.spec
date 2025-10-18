%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rlibkriging
%global packver   0.9-2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.2.3
Release:          1%{?dist}%{?buildtag}
Summary:          Kriging Models using the 'libKriging' Library

License:          Apache License (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    cmake
BuildRequires:    R-devel >= 4.2
Requires:         R-core >= 4.2
BuildRequires:    R-CRAN-Rcpp >= 1.0.12
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-DiceKriging 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 1.0.12
Requires:         R-methods 
Requires:         R-CRAN-DiceKriging 

%description
Interface to 'libKriging' 'C++' library <https://github.com/libKriging>
that should provide most standard Kriging / Gaussian process regression
features (like in 'DiceKriging', 'kergp' or 'RobustGaSP' packages).
'libKriging' relies on Armadillo linear algebra library (Apache 2 license)
by Conrad Sanderson, 'lbfgsb_cpp' is a 'C++' port around by Pascal Have of
'lbfgsb' library (BSD-3 license) by Ciyou Zhu, Richard Byrd, Jorge Nocedal
and Jose Luis Morales used for hyperparameters optimization.

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
