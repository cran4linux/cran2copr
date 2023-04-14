%global __brp_check_rpaths %{nil}
%global packname  ktsolve
%global packver   1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3
Release:          3%{?dist}%{?buildtag}
Summary:          Configurable Function for Solving Families of NonlinearEquations

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-BB 
BuildRequires:    R-CRAN-nleqslv 
Requires:         R-methods 
Requires:         R-CRAN-BB 
Requires:         R-CRAN-nleqslv 

%description
This is designed for use with an arbitrary set of equations with an
arbitrary set of unknowns. The user selects "fixed" values for enough
unknowns to leave as many variables as there are equations, which in most
cases means the system is properly defined and a unique solution exists.
The function, the fixed values and initial values for the remaining
unknowns are fed to a nonlinear backsolver. The original version of
"TK!Solver" , now a product of Universal Technical Systems
(<https://www.uts.com>) was the inspiration for this function.

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
%{rlibdir}/%{packname}
