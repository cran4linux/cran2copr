%global packname  RcppEigenAD
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}
Summary:          Compiles 'C++' Code using 'Rcpp', 'Eigen' and 'CppAD' to ProduceFirst and Second Order Partial Derivatives

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.12.12
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RcppEigen 
BuildRequires:    R-CRAN-functional 
BuildRequires:    R-CRAN-memoise 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-Rcpp >= 0.12.12
Requires:         R-methods 
Requires:         R-CRAN-RcppEigen 
Requires:         R-CRAN-functional 
Requires:         R-CRAN-memoise 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-Rdpack 

%description
Compiles 'C++' code using 'Rcpp', 'Eigen' and 'CppAD' to produce first and
second order partial derivatives. Also provides an implementation of Faa'
di Bruno's formula to combine the partial derivatives of composed
functions, (see Hardy, M (2006) <arXiv:math/0601149v1>).

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
%{rlibdir}/%{packname}/include
%doc %{rlibdir}/%{packname}/REFERENCES.bib
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
