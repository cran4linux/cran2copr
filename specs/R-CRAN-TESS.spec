%global packname  TESS
%global packver   2.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.0
Release:          3%{?dist}
Summary:          Diversification Rate Estimation and Fast Simulation ofReconstructed Phylogenetic Trees under Tree-WideTime-Heterogeneous Birth-Death Processes IncludingMass-Extinction Events

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.11.0
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-deSolve 
Requires:         R-CRAN-Rcpp >= 0.11.0
Requires:         R-CRAN-ape 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-deSolve 

%description
Simulation of reconstructed phylogenetic trees under tree-wide
time-heterogeneous birth-death processes and estimation of diversification
parameters under the same model. Speciation and extinction rates can be
any function of time and mass-extinction events at specific times can be
provided. Trees can be simulated either conditioned on the number of
species, the time of the process, or both. Additionally, the likelihood
equations are implemented for convenience and can be used for Maximum
Likelihood (ML) estimation and Bayesian inference.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
