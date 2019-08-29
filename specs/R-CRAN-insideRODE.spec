%global packname  insideRODE
%global packver   2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0
Release:          1%{?dist}
Summary:          insideRODE includes buildin functions with deSolve solver andC/FORTRAN interfaces to nlme, together with compiled codes.

License:          LGPL (> 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.13.0
Requires:         R-core >= 2.13.0
BuildArch:        noarch
BuildRequires:    R-CRAN-deSolve 
BuildRequires:    R-nlme 
BuildRequires:    R-lattice 
Requires:         R-CRAN-deSolve 
Requires:         R-nlme 
Requires:         R-lattice 

%description
insideRODE package includes buildin functions from deSolve, compiled
functions from compiler, and C/FORTRAN code interfaces to nlme. It
includes nlmLSODA, nlmODE, nlmVODE,nlmLSODE for general purpose;
cfLSODA,cfLSODE, cfODE, cfVODE call C/FORTRAN compiled dll
functions.ver2.0 add sink()function into example it helps to directly
combine c/fortran source code in R files. Finally, with new compiler
package, we generated compiled functions: nlmODEcp, nlmVODEcp,
nlmLSODEcp,nlmLSODAcp and cpODE, cpLSODA, cpLSODE, cpVODE. They will help
to increase speed.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
