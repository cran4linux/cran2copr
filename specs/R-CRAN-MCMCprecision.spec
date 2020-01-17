%global packname  MCMCprecision
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}
Summary:          Precision of Discrete Parameters in Transdimensional MCMC

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-parallel 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-combinat 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-RcppProgress 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-Rcpp 
Requires:         R-parallel 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-Matrix 
Requires:         R-CRAN-combinat 

%description
Estimates the precision of transdimensional Markov chain Monte Carlo
(MCMC) output, which is often used for Bayesian analysis of models with
different dimensionality (e.g., model selection). Transdimensional MCMC
(e.g., reversible jump MCMC) relies on sampling a discrete model-indicator
variable to estimate the posterior model probabilities. If only few
switches occur between the models, precision may be low and assessment
based on the assumption of independent samples misleading. Based on the
observed transition matrix of the indicator variable, the method of Heck,
Overstall, Gronau, & Wagenmakers (2019, Statistics & Computing, 29,
631-643) <doi:10.1007/s11222-018-9828-0> draws posterior samples of the
stationary distribution to (a) assess the uncertainty in the estimated
posterior model probabilities and (b) estimate the effective sample size
of the MCMC output.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/include
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
