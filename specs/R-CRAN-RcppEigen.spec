%global packname  RcppEigen
%global packver   0.3.3.7.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.3.7.0
Release:          3%{?dist}%{?buildtag}
Summary:          'Rcpp' Integration for the 'Eigen' Templated Linear AlgebraLibrary

License:          GPL (>= 2) | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.1
Requires:         R-core >= 2.15.1
BuildRequires:    R-Matrix >= 1.1.0
BuildRequires:    R-CRAN-Rcpp >= 0.11.0
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-Matrix >= 1.1.0
Requires:         R-CRAN-Rcpp >= 0.11.0
Requires:         R-stats 
Requires:         R-utils 

%description
R and 'Eigen' integration using 'Rcpp'. 'Eigen' is a C++ template library
for linear algebra: matrices, vectors, numerical solvers and related
algorithms.  It supports dense and sparse matrices on integer, floating
point and complex numbers, decompositions of such matrices, and solutions
of linear systems. Its performance on many algorithms is comparable with
some of the best implementations based on 'Lapack' and level-3 'BLAS'. The
'RcppEigen' package includes the header files from the 'Eigen' C++
template library (currently version 3.3.4). Thus users do not need to
install 'Eigen' itself in order to use 'RcppEigen'. Since version 3.1.1,
'Eigen' is licensed under the Mozilla Public License (version 2); earlier
version were licensed under the GNU LGPL version 3 or later. 'RcppEigen'
(the 'Rcpp' bindings/bridge to 'Eigen') is licensed under the GNU GPL
version 2 or later, as is the rest of 'Rcpp'.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/COPYRIGHTS
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/include
%doc %{rlibdir}/%{packname}/NEWS.Rd
%doc %{rlibdir}/%{packname}/skeleton
%doc %{rlibdir}/%{packname}/tinytest
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
