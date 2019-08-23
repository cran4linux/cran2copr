%global packname  RcppGSL
%global packver   0.3.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.6
Release:          1%{?dist}
Summary:          'Rcpp' Integration for 'GNU GSL' Vectors and Matrices

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz

BuildRequires:    gsl-devel
Requires:         gsl-devel
BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.11.0
BuildRequires:    R-stats 
Requires:         R-CRAN-Rcpp >= 0.11.0
Requires:         R-stats 

%description
'Rcpp' integration for 'GNU GSL' vectors and matrices The 'GNU Scientific
Library' (or 'GSL') is a collection of numerical routines for scientific
computing. It is particularly useful for C and C++ programs as it provides
a standard C interface to a wide range of mathematical routines. There are
over 1000 functions in total with an extensive test suite. The 'RcppGSL'
package provides an easy-to-use interface between 'GSL' data structures
and R using concepts from 'Rcpp' which is itself a package that eases the
interfaces between R and C++. This package also serves as a prime example
of how to build a package that uses 'Rcpp' to connect to another
third-party library. The 'autoconf' script, 'inline' plugin and example
package can all be used as a stanza to write a similar package against
another library.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/include
%doc %{rlibdir}/%{packname}/NEWS.Rd
%doc %{rlibdir}/%{packname}/skeleton
%doc %{rlibdir}/%{packname}/unitTests
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
