%global packname  coala
%global packver   0.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.0
Release:          3%{?dist}
Summary:          A Framework for Coalescent Simulation

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-CRAN-rehh >= 3.0.0
BuildRequires:    R-CRAN-R6 >= 2.0.1
BuildRequires:    R-CRAN-scrm >= 1.6.0.2
BuildRequires:    R-CRAN-RcppArmadillo >= 0.3.810.0
BuildRequires:    R-CRAN-Rcpp >= 0.11.0
BuildRequires:    R-CRAN-assertthat >= 0.1
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-rehh >= 3.0.0
Requires:         R-CRAN-R6 >= 2.0.1
Requires:         R-CRAN-scrm >= 1.6.0.2
Requires:         R-CRAN-Rcpp >= 0.11.0
Requires:         R-CRAN-assertthat >= 0.1
Requires:         R-CRAN-digest 
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-utils 

%description
Coalescent simulators can rapidly simulate biological sequences evolving
according to a given model of evolution. You can use this package to
specify such models, to conduct the simulations and to calculate
additional statistics from the results. It relies on existing simulators
for doing the simulation, and currently supports the programs 'ms', 'msms'
and 'scrm'. It also supports finite-sites mutation models by combining the
simulators with the program 'seq-gen'.

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
%doc %{rlibdir}/%{packname}/example_fasta_files
%{rlibdir}/%{packname}/include
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
