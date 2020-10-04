%global packname  bayesdistreg
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Bayesian Distribution Regression

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.1.0
Requires:         R-core >= 2.1.0
BuildArch:        noarch
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-stats 
Requires:         R-MASS 
Requires:         R-CRAN-sandwich 
Requires:         R-stats 

%description
Implements Bayesian Distribution Regression methods. This package contains
functions for three estimators (non-asymptotic, semi-asymptotic and
asymptotic) and related routines for Bayesian Distribution Regression in
Huang and Tsyawo (2018) <doi:10.2139/ssrn.3048658> which is also the
recommended reference to cite for this package. The functions can be
grouped into three (3) categories. The first computes the logit likelihood
function and posterior densities under uniform and normal priors. The
second contains Independence and Random Walk Metropolis-Hastings Markov
Chain Monte Carlo (MCMC) algorithms as functions and the third category of
functions are useful for semi-asymptotic and asymptotic Bayesian
distribution regression inference.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
