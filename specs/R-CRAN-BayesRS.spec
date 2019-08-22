%global packname  BayesRS
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}
Summary:          Bayes Factors for Hierarchical Linear Models with ContinuousPredictors

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rjags 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-metRology 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-reshape 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-coda 
Requires:         R-CRAN-rjags 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-metRology 
Requires:         R-grid 
Requires:         R-CRAN-reshape 
Requires:         R-methods 
Requires:         R-CRAN-coda 

%description
Runs hierarchical linear Bayesian models. Samples from the posterior
distributions of model parameters in JAGS (Just Another Gibbs Sampler;
Plummer, 2017, <http://mcmc-jags.sourceforge.net>). Computes Bayes factors
for group parameters of interest with the Savage-Dickey density ratio
(Wetzels, Raaijmakers, Jakab, Wagenmakers, 2009,
<doi:10.3758/PBR.16.4.752>).

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
