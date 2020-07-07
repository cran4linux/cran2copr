%global packname  MCMCpack
%global packver   1.4-8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.8
Release:          3%{?dist}
Summary:          Markov Chain Monte Carlo (MCMC) Package

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildRequires:    R-CRAN-coda >= 0.11.3
BuildRequires:    R-MASS 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-lattice 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-mcmc 
BuildRequires:    R-CRAN-quantreg 
Requires:         R-CRAN-coda >= 0.11.3
Requires:         R-MASS 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-lattice 
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-CRAN-mcmc 
Requires:         R-CRAN-quantreg 

%description
Contains functions to perform Bayesian inference using posterior
simulation for a number of statistical models. Most simulation is done in
compiled C++ written in the Scythe Statistical Library Version 1.0.3. All
models return 'coda' mcmc objects that can then be summarized using the
'coda' package. Some useful utility functions such as density functions,
pseudo-random number generators for statistical distributions, a general
purpose Metropolis sampling algorithm, and tools for visualization are
provided.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%doc %{rlibdir}/%{packname}/HISTORY.txt
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
