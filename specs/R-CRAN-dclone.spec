%global packname  dclone
%global packver   2.3-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3.0
Release:          3%{?dist}%{?buildtag}
Summary:          Data Cloning and MCMC Tools for Maximum Likelihood Methods

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.1
Requires:         R-core >= 2.15.1
BuildArch:        noarch
BuildRequires:    R-CRAN-rjags >= 4.4
BuildRequires:    R-CRAN-coda >= 0.13
BuildRequires:    R-parallel 
BuildRequires:    R-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-rstan 
Requires:         R-CRAN-rjags >= 4.4
Requires:         R-CRAN-coda >= 0.13
Requires:         R-parallel 
Requires:         R-Matrix 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-rstan 

%description
Low level functions for implementing maximum likelihood estimating
procedures for complex models using data cloning and Bayesian Markov chain
Monte Carlo methods as described in Solymos 2010 (R Journal 2(2):29--37).
Sequential and parallel MCMC support for 'JAGS', 'WinBUGS', 'OpenBUGS',
and 'Stan'.

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
%{rlibdir}/%{packname}/INDEX
