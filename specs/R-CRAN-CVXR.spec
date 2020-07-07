%global packname  CVXR
%global packver   1.0-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          3%{?dist}
Summary:          Disciplined Convex Optimization

License:          Apache License 2.0 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-scs >= 1.3
BuildRequires:    R-CRAN-ECOSolveR >= 0.5.3
BuildRequires:    R-CRAN-Rcpp >= 0.12.12
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-bit64 
BuildRequires:    R-CRAN-gmp 
BuildRequires:    R-CRAN-Rmpfr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-osqp 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-scs >= 1.3
Requires:         R-CRAN-ECOSolveR >= 0.5.3
Requires:         R-CRAN-Rcpp >= 0.12.12
Requires:         R-methods 
Requires:         R-CRAN-R6 
Requires:         R-Matrix 
Requires:         R-CRAN-bit64 
Requires:         R-CRAN-gmp 
Requires:         R-CRAN-Rmpfr 
Requires:         R-stats 
Requires:         R-CRAN-osqp 

%description
An object-oriented modeling language for disciplined convex programming
(DCP). It allows the user to formulate convex optimization problems in a
natural way following mathematical convention and DCP rules. The system
analyzes the problem, verifies its convexity, converts it into a canonical
form, and hands it off to an appropriate solver to obtain the solution.

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
%{rlibdir}/%{packname}/data
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/include
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
