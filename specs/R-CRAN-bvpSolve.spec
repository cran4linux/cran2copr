%global packname  bvpSolve
%global packver   1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4
Release:          3%{?dist}
Summary:          Solvers for Boundary Value Problems of Differential Equations

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.01
Requires:         R-core >= 2.01
BuildRequires:    R-CRAN-deSolve 
BuildRequires:    R-CRAN-rootSolve 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-deSolve 
Requires:         R-CRAN-rootSolve 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 

%description
Functions that solve boundary value problems ('BVP') of systems of
ordinary differential equations ('ODE') and differential algebraic
equations ('DAE'). The functions provide an interface to the FORTRAN
functions 'twpbvpC', 'colnew/colsys', and an R-implementation of the
shooting method. 'Mazzia, F., J.R. Cash and K. Soetaert, 2014.
<DOI:10.7494/OpMath.2014.34.2.387>.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
