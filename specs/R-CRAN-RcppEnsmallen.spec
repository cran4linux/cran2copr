%global packname  RcppEnsmallen
%global packver   0.2.11.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.11.3.1
Release:          1%{?dist}
Summary:          Header-Only C++ Mathematical Optimization Library for'Armadillo'

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-RcppArmadillo >= 0.8.400.0.0
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
terms. Note that 'Ensmallen' requires a compiler that supports 'C++11' and
'Armadillo' 8.400 or later.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/AUTHORS
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/COPYRIGHTS
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/include
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
