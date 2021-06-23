%global __brp_check_rpaths %{nil}
%global packname  deBInfer
%global packver   0.4.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.2
Release:          3%{?dist}%{?buildtag}
Summary:          Bayesian Inference for Differential Equations

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-deSolve 
BuildRequires:    R-CRAN-truncdist 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-MASS 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-PBSddesolve 
BuildRequires:    R-methods 
Requires:         R-CRAN-deSolve 
Requires:         R-CRAN-truncdist 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-MASS 
Requires:         R-stats 
Requires:         R-CRAN-mvtnorm 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-PBSddesolve 
Requires:         R-methods 

%description
A Bayesian framework for parameter inference in differential equations.
This approach offers a rigorous methodology for parameter inference as
well as modeling the link between unobservable model states and
parameters, and observable quantities. Provides templates for the DE
model, the observation model and data likelihood, and the model parameters
and their prior distributions. A Markov chain Monte Carlo (MCMC) procedure
processes these inputs to estimate the posterior distributions of the
parameters and any derived quantities, including the model trajectories.
Further functionality is provided to facilitate MCMC diagnostics and the
visualisation of the posterior distributions of model parameters and
trajectories.

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
%{rlibdir}/%{packname}/INDEX
