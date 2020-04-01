%global packname  sqp
%global packver   0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5
Release:          1%{?dist}
Summary:          (Sequential) Quadratic Programming

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 1.0.0
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-Rcpp >= 1.0.0
Requires:         R-Matrix 
Requires:         R-CRAN-Rdpack 

%description
Solving procedures for quadratic programming with optional equality and
inequality constraints, which can be used for by sequential quadratic
programming (SQP). Similar to Newton-Raphson methods in the unconstrained
case, sequential quadratic programming solves non-linear constrained
optimization problems by iteratively solving linear approximations of the
optimality conditions of such a problem (cf. Powell (1978)
<doi:10.1007/BFb0067703>; Nocedal and Wright (1999, ISBN:
978-0-387-98793-4)). The Hessian matrix in this strategy is commonly
approximated by the BFGS method in its damped modification proposed by
Powell (1978) <doi:10.1007/BFb0067703>. All methods are implemented in C++
as header-only library, such that it is easy to use in other packages.

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
%{rlibdir}/%{packname}/include
%doc %{rlibdir}/%{packname}/REFERENCES.bib
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
