%global packname  optiSolve
%global packver   0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1
Release:          1%{?dist}
Summary:          Linear, Quadratic, and Rational Optimization

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.2
Requires:         R-core >= 3.3.2
BuildArch:        noarch
BuildRequires:    R-CRAN-Rcpp >= 0.12.4
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-shapes 
BuildRequires:    R-CRAN-Rcsdp 
BuildRequires:    R-CRAN-alabama 
BuildRequires:    R-CRAN-cccp 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-MASS 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-stats 
Requires:         R-CRAN-Rcpp >= 0.12.4
Requires:         R-Matrix 
Requires:         R-CRAN-shapes 
Requires:         R-CRAN-Rcsdp 
Requires:         R-CRAN-alabama 
Requires:         R-CRAN-cccp 
Requires:         R-CRAN-nloptr 
Requires:         R-MASS 
Requires:         R-methods 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-stringr 
Requires:         R-stats 

%description
Solver for linear, quadratic, and rational programs with linear,
quadratic, and rational constraints. A unified interface to different R
packages is provided. Optimization problems are transformed into
equivalent formulations and solved by the respective package. For example,
quadratic programming problems with linear, quadratic and rational
constraints can be solved by augmented Lagrangian minimization using
package 'alabama', or by sequential quadratic programming using solver
'slsqp'.  Alternatively, they can be reformulated as optimization problems
with second order cone constraints and solved with package 'cccp', or
transformed into semidefinite programming problems and solved using solver
'csdp'.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
