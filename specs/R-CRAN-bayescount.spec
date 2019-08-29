%global packname  bayescount
%global packver   0.9.99-5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.99.5
Release:          1%{?dist}
Summary:          Power Calculations and Bayesian Analysis of Count Distributionsand FECRT Data using MCMC

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.0
Requires:         R-core >= 2.14.0
BuildRequires:    R-CRAN-runjags >= 2.0.1
BuildRequires:    R-CRAN-rjags 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-runjags >= 2.0.1
Requires:         R-CRAN-rjags 
Requires:         R-CRAN-coda 
Requires:         R-stats 
Requires:         R-utils 

%description
A set of functions to allow analysis of count data (such as faecal egg
count data) using Bayesian MCMC methods.  Returns information on the
possible values for mean count, coefficient of variation and zero
inflation (true prevalence) present in the data.  A complete faecal egg
count reduction test (FECRT) model is implemented, which returns inference
on the true efficacy of the drug from the pre- and post-treatment data
provided, using non-parametric bootstrapping as well as using Bayesian
MCMC.  Functions to perform power analyses for faecal egg counts
(including FECRT) are also provided.

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
%{rlibdir}/%{packname}/libs
