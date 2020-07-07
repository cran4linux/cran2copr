%global packname  diversitree
%global packver   0.9-13
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.13
Release:          3%{?dist}
Summary:          Comparative 'Phylogenetic' Analyses of Diversification

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    fftw-devel >= 3.1.2
BuildRequires:    gsl-devel >= 1.15
Requires:         fftw
Requires:         gsl
BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-deSolve >= 1.7
BuildRequires:    R-CRAN-Rcpp >= 0.10.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-subplex 
Requires:         R-CRAN-deSolve >= 1.7
Requires:         R-CRAN-Rcpp >= 0.10.0
Requires:         R-methods 
Requires:         R-CRAN-ape 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-CRAN-subplex 

%description
Contains a number of comparative 'phylogenetic' methods, mostly focusing
on analysing diversification and character evolution.  Contains
implementations of 'BiSSE' (Binary State 'Speciation' and Extinction) and
its unresolved tree extensions, 'MuSSE' (Multiple State 'Speciation' and
Extinction), 'QuaSSE', 'GeoSSE', and 'BiSSE-ness' Other included methods
include Markov models of discrete and continuous trait evolution and
constant rate 'speciation' and extinction.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/CONTRIBUTORS.md
%doc %{rlibdir}/%{packname}/tests
%doc %{rlibdir}/%{packname}/update-gh-pages.sh
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
