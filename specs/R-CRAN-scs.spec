%global packname  scs
%global packver   1.3-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.2
Release:          3%{?dist}
Summary:          Splitting Conic Solver

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15
Requires:         R-core >= 2.15

%description
Solves convex cone programs via operator splitting. Can solve: linear
programs ('LPs'), second-order cone programs ('SOCPs'), semidefinite
programs ('SDPs'), exponential cone programs ('ECPs'), and power cone
programs ('PCPs'), or problems with any combination of those cones. 'SCS'
uses 'AMD' (a set of routines for permuting sparse matrices prior to
factorization) and 'LDL' (a sparse 'LDL' factorization and solve package)
from 'SuiteSparse' (<http://www.suitesparse.com>).

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
