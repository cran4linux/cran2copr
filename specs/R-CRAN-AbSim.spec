%global packname  AbSim
%global packver   0.2.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.6
Release:          3%{?dist}%{?buildtag}
Summary:          Time Resolved Simulations of Antibody Repertoires

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-poweRlaw 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-poweRlaw 

%description
Simulation methods for the evolution of antibody repertoires. The heavy
and light chain variable region of both human and C57BL/6 mice can be
simulated in a time-dependent fashion. Both single lineages using one set
of V-, D-, and J-genes or full repertoires can be simulated. The algorithm
begins with an initial V-D-J recombination event, starting the first
phylogenetic tree. Upon completion, the main loop of the algorithm begins,
with each iteration representing one simulated time step. Various mutation
events are possible at each time step, contributing to a diverse final
repertoire.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
