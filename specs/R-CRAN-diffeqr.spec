%global packname  diffeqr
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}
Summary:          Solving Differential Equations (ODEs, SDEs, DDEs, DAEs)

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-JuliaCall 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-JuliaCall 
Requires:         R-CRAN-stringr 

%description
An interface to 'DifferentialEquations.jl'
<http://docs.juliadiffeq.org/latest/> from the R programming language. It
has unique high performance methods for solving ordinary differential
equations (ODE), stochastic differential equations (SDE), delay
differential equations (DDE), differential-algebraic equations (DAE), and
more. Much of the functionality, including features like adaptive time
stepping in SDEs, are unique and allow for multiple orders of magnitude
speedup over more common methods. 'diffeqr' attaches an R interface onto
the package, allowing seamless use of this tooling by R users.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
