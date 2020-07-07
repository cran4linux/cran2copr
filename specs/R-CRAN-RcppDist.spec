%global packname  RcppDist
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          3%{?dist}
Summary:          'Rcpp' Integration of Additional Probability Distributions

License:          GPL (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp 

%description
The 'Rcpp' package provides a C++ library to make it easier to use C++
with R. R and 'Rcpp' provide functions for a variety of statistical
distributions. Several R packages make functions available to R for
additional statistical distributions. However, to access these functions
from C++ code, a costly call to the R functions must be made. 'RcppDist'
provides a header-only C++ library with functions for additional
statistical distributions that can be called from C++ when writing code
using 'Rcpp' or 'RcppArmadillo'. Functions are available that return a
'NumericVector' as well as doubles, and for multivariate or matrix
distributions, 'Armadillo' vectors and matrices. 'RcppDist' provides
functions for the following distributions: the four parameter beta
distribution; the location- scale t distribution; the truncated normal
distribution; the truncated t distribution; a truncated location-scale t
distribution; the triangle distribution; the multivariate normal
distribution*; the multivariate t distribution*; the Wishart
distribution*; and the inverse Wishart distribution*. Distributions marked
with an asterisk rely on 'RcppArmadillo'.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/include
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
