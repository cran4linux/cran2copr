%global packname  BayesSummaryStatLM
%global packver   1.0-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          3%{?dist}
Summary:          MCMC Sampling of Bayesian Linear Models via Summary Statistics

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.1
Requires:         R-core >= 3.1.1
BuildArch:        noarch
BuildRequires:    R-CRAN-mvnfast 
BuildRequires:    R-CRAN-ff 
Requires:         R-CRAN-mvnfast 
Requires:         R-CRAN-ff 

%description
Methods for generating Markov Chain Monte Carlo (MCMC) posterior samples
of Bayesian linear regression model parameters that require only summary
statistics of data as input. Summary statistics are useful for systems
with very limited amounts of physical memory. The package provides two
functions: one function that computes summary statistics of data and one
function that carries out the MCMC posterior sampling for Bayesian linear
regression models where summary statistics are used as input. The function
read.regress.data.ff utilizes the R package 'ff' to handle data sets that
are too large to fit into a user's physical memory, by reading in data in
chunks.

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
%{rlibdir}/%{packname}/INDEX
