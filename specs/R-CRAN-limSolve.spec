%global __brp_check_rpaths %{nil}
%global packname  limSolve
%global packver   1.5.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.6
Release:          3%{?dist}%{?buildtag}
Summary:          Solving Linear Inverse Models

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-CRAN-lpSolve 
BuildRequires:    R-MASS 
Requires:         R-CRAN-quadprog 
Requires:         R-CRAN-lpSolve 
Requires:         R-MASS 

%description
Functions that (1) find the minimum/maximum of a linear or quadratic
function: min or max (f(x)), where f(x) = ||Ax-b||^2 or f(x) =
sum(a_i*x_i) subject to equality constraints Ex=f and/or inequality
constraints Gx>=h, (2) sample an underdetermined- or overdetermined system
Ex=f subject to Gx>=h, and if applicable Ax~=b, (3) solve a linear system
Ax=B for the unknown x. It includes banded and tridiagonal linear systems.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/COPYRIGHTS
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
