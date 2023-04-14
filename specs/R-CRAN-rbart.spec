%global __brp_check_rpaths %{nil}
%global packname  rbart
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Bayesian Trees for Conditional Mean and Variance

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-Rcpp >= 0.12.3
Requires:         R-CRAN-Rcpp >= 0.12.3

%description
A model of the form Y = f(x) + s(x) Z is fit where functions f and s are
modeled with ensembles of trees and Z is standard normal. This model is
developed in the paper 'Heteroscedastic BART Via Multiplicative Regression
Trees' (Pratola, Chipman, George, and McCulloch, 2019,
<arXiv:1709.07542v2>). BART refers to Bayesian Additive Regression Trees.
See the R-package 'BART'. The predictor vector x may be high dimensional.
A Markov Chain Monte Carlo (MCMC) algorithm provides Bayesian posterior
uncertainty for both f and s. The MCMC uses the recent innovations in
Efficient Metropolis--Hastings proposal mechanisms for Bayesian regression
tree models (Pratola, 2015, Bayesian Analysis, <doi:10.1214/16-BA999>).

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
