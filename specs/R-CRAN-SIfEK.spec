%global __brp_check_rpaths %{nil}
%global packname  SIfEK
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Statistical Inference for Enzyme Kinetics

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildArch:        noarch
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-ramcmc 
BuildRequires:    R-CRAN-smfsb 
BuildRequires:    R-CRAN-numDeriv 
Requires:         R-MASS 
Requires:         R-CRAN-ramcmc 
Requires:         R-CRAN-smfsb 
Requires:         R-CRAN-numDeriv 

%description
Functions for estimating catalytic constant and Michaelis-Menten constant
(MM constant) of stochastic Michaelis-Menten enzyme kinetics model are
provided. The likelihood functions based on stochastic simulation
approximation (SSA), diffusion approximation (DA), and Gaussian processes
(GP) are provided to construct posterior functions for the Bayesian
estimation. All functions utilize Markov Chain Monte Carlo (MCMC) methods
with Metropolis- Hastings algorithm with random walk chain and robust
adaptive Metropolis-Hastings algorithm based on Bayesian framework.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
