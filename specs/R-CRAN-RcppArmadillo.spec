%global packname  RcppArmadillo
%global packver   0.9.900.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.900.2.0
Release:          1%{?dist}
Summary:          'Rcpp' Integration for the 'Armadillo' Templated Linear AlgebraLibrary

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-Rcpp >= 0.11.0
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-methods 
Requires:         R-CRAN-Rcpp >= 0.11.0
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-methods 

%description
'Armadillo' is a templated C++ linear algebra library (by Conrad
Sanderson) that aims towards a good balance between speed and ease of use.
Integer, floating point and complex numbers are supported, as well as a
subset of trigonometric and statistics functions. Various matrix
decompositions are provided through optional integration with LAPACK and
ATLAS libraries. The 'RcppArmadillo' package includes the header files
from the templated 'Armadillo' library. Thus users do not need to install
'Armadillo' itself in order to use 'RcppArmadillo'. From release 7.800.0
on, 'Armadillo' is licensed under Apache License 2; previous releases were
under licensed as MPL 2.0 from version 3.800.0 onwards and LGPL-3 prior to
that; 'RcppArmadillo' (the 'Rcpp' bindings/bridge to Armadillo) is
licensed under the GNU GPL version 2 or later, as is the rest of 'Rcpp'.
Note that Armadillo requires a fairly recent compiler; for the g++ family
at least version 4.6.* is required.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
