%global packname  RSiena
%global packver   1.2-12
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.12
Release:          1%{?dist}
Summary:          Siena - Simulation Investigation for Empirical Network Analysis

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    make
Requires:         tcl >= 8.5
Requires:         tk >= 8.5
BuildRequires:    R-devel >= 2.15.0
Requires:         R-core >= 2.15.0
BuildRequires:    R-utils 
BuildRequires:    R-Matrix 
BuildRequires:    R-tcltk 
BuildRequires:    R-lattice 
BuildRequires:    R-parallel 
BuildRequires:    R-MASS 
BuildRequires:    R-methods 
Requires:         R-utils 
Requires:         R-Matrix 
Requires:         R-tcltk 
Requires:         R-lattice 
Requires:         R-parallel 
Requires:         R-MASS 
Requires:         R-methods 

%description
The main purpose of this package is to perform simulation-based estimation
of stochastic actor-oriented models for longitudinal network data
collected as panel data. Dependent variables can be single or multivariate
networks, which can be directed, non-directed, or two-mode. There are also
functions for testing parameters and checking goodness of fit. An overview
of these models is given in Tom A.B. Snijders (2017), Stochastic
Actor-Oriented Models for Network Dynamics, Annual Review of Statistics
and Its Application, 4, 343-363 <doi:
10.1146/annurev-statistics-060116-054035>.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/examples
%doc %{rlibdir}/%{packname}/ilcampo.gif
%doc %{rlibdir}/%{packname}/scripts
%doc %{rlibdir}/%{packname}/sienascript
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
