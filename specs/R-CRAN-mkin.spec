%global packname  mkin
%global packver   0.9.49.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.49.8
Release:          1%{?dist}
Summary:          Kinetic Evaluation of Chemical Degradation Data

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-deSolve 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-inline 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-lmtest 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-CRAN-deSolve 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-inline 
Requires:         R-parallel 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-lmtest 

%description
Calculation routines based on the FOCUS Kinetics Report (2006, 2014).
Includes a function for conveniently defining differential equation
models, model solution based on eigenvalues if possible or using numerical
solvers and a choice of the optimisation methods made available by the
'FME' package.  If a C compiler (on windows: 'Rtools') is installed,
differential equation models are solved using compiled C functions.
Please note that no warranty is implied for correctness of results or
fitness for a particular purpose.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/testdata
%{rlibdir}/%{packname}/INDEX
