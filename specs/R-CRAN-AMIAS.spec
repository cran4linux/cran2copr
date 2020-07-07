%global packname  AMIAS
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          3%{?dist}
Summary:          Alternating Minimization Induced Active Set Algorithms

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-limSolve 
BuildRequires:    R-Matrix 
Requires:         R-utils 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-limSolve 
Requires:         R-Matrix 

%description
An implementation of alternating minimization induced active set (AMIAS)
method for solving the generalized L0 problem. The AMIAS method is based
on the necessary optimality conditions derived from an augmented
Lagrangian framework. The proposed method takes full advantage of the
primal and dual variables with complementary supports, and decouples the
high-dimensional problem into two sub-systems on the active and inactive
sets, respectively. A sequential AMIAS algorithm with warm start
initialization is developed for efficient determination of the cardinality
parameter, along with the output of solution paths.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
