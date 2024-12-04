%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RcppEnsmallen
%global packver   0.2.22.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.22.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Header-Only C++ Mathematical Optimization Library for 'Armadillo'

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-RcppArmadillo >= 0.10.8.2.0
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-Rcpp 

%description
'Ensmallen' is a templated C++ mathematical optimization library (by the
'MLPACK' team) that provides a simple set of abstractions for writing an
objective function to optimize. Provided within are various standard and
cutting-edge optimizers that include full-batch gradient descent
techniques, small-batch techniques, gradient-free optimizers, and
constrained optimization. The 'RcppEnsmallen' package includes the header
files from the 'Ensmallen' library and pairs the appropriate header files
from 'armadillo' through the 'RcppArmadillo' package. Therefore, users do
not need to install 'Ensmallen' nor 'Armadillo' to use 'RcppEnsmallen'.
Note that 'Ensmallen' is licensed under 3-Clause BSD, 'Armadillo' starting
from 7.800.0 is licensed under Apache License 2, 'RcppArmadillo' (the
'Rcpp' bindings/bridge to 'Armadillo') is licensed under the GNU GPL
version 2 or later. Thus, 'RcppEnsmallen' is also licensed under similar
terms. Note that 'Ensmallen' requires a compiler that supports 'C++14' and
'Armadillo' 10.8.2 or later.

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
