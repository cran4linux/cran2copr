%global packname  EntropyMCMC
%global packver   1.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          2%{?dist}
Summary:          MCMC Simulation and Convergence Evaluation using Entropy andKullback-Leibler Divergence Estimation

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildRequires:    R-CRAN-RANN 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-mixtools 
Requires:         R-CRAN-RANN 
Requires:         R-parallel 
Requires:         R-CRAN-mixtools 

%description
Tools for Markov Chain Monte Carlo (MCMC) simulation and performance
analysis. Simulate MCMC algorithms including adaptive MCMC, evaluate their
convergence rate, and compare candidate MCMC algorithms for a same target
density, based on entropy and Kullback-Leibler divergence criteria. MCMC
algorithms can be simulated using provided functions, or imported from
external codes. This package is based upon work starting with Chauveau, D.
and Vandekerkhove, P. (2013) <doi:10.1051/ps/2012004> and next articles.

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
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
