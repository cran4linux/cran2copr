%global packname  parallelMCMCcombine
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Methods for combining independent subset Markov chain MonteCarlo (MCMC) posterior samples to estimate a posterior densitygiven the full data set

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-CRAN-mvtnorm 

%description
Recent Bayesian Markov chain Monto Carlo (MCMC) methods have been
developed for big data sets that are too large to be analyzed using
traditional statistical methods. These methods partition the data into
non-overlapping subsets, and perform parallel independent Bayesian MCMC
analyses on the data subsets, creating independent subposterior samples
for each data subset. These independent subposterior samples are combined
through four functions in this package, including averaging across subset
samples, weighted averaging across subsets samples, and kernel smoothing
across subset samples. The four functions assume the user has previously
run the Bayesian analysis and has produced the independent subposterior
samples outside of the package; the functions use as input the array of
subposterior samples. The methods have been demonstrated to be useful for
Bayesian MCMC models including Bayesian logistic regression, Bayesian
Gaussian mixture models and Bayesian hierarchical Poisson-Gamma models.
The methods are appropriate for Bayesian hierarchical models with
hyperparameters, as long as data values in a single level of the hierarchy
are not split into subsets.

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
%{rlibdir}/%{packname}/INDEX
