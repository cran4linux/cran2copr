%global packname  runjags
%global packver   2.0.4-6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.4.6
Release:          3%{?dist}
Summary:          Interface Utilities, Model Templates, Parallel Computing Methodsand Additional Distributions for MCMC Models in JAGS

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    jags-devel
Requires:         jags
BuildRequires:    R-devel >= 2.14.0
Requires:         R-core >= 2.14.0
BuildRequires:    R-lattice >= 0.20.10
BuildRequires:    R-CRAN-coda >= 0.17.1
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-lattice >= 0.20.10
Requires:         R-CRAN-coda >= 0.17.1
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-utils 

%description
User-friendly interface utilities for MCMC models via Just Another Gibbs
Sampler (JAGS), facilitating the use of parallel (or distributed)
processors for multiple chains, automated control of convergence and
sample length diagnostics, and evaluation of the performance of a model
using drop-k validation or against simulated data. Template model
specifications can be generated using a standard lme4-style formula
interface to assist users less familiar with the BUGS syntax.  A JAGS
extension module provides additional distributions including the Pareto
family of distributions, the DuMouchel prior and the half-Cauchy prior.

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/xgrid
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
