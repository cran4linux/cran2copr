%global packname  BiProbitPartial
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}
Summary:          Bivariate Probit with Partial Observability

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-optimr >= 2016.8.16
BuildRequires:    R-CRAN-numDeriv >= 2016.8.1
BuildRequires:    R-CRAN-Formula >= 1.2.3
BuildRequires:    R-CRAN-mvtnorm >= 1.0.8
BuildRequires:    R-CRAN-pbivnorm >= 0.6.0
BuildRequires:    R-CRAN-RcppTN >= 0.2.2
BuildRequires:    R-CRAN-coda >= 0.19.2
BuildRequires:    R-CRAN-Rcpp >= 0.12.19
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-optimr >= 2016.8.16
Requires:         R-CRAN-numDeriv >= 2016.8.1
Requires:         R-CRAN-Formula >= 1.2.3
Requires:         R-CRAN-mvtnorm >= 1.0.8
Requires:         R-CRAN-pbivnorm >= 0.6.0
Requires:         R-CRAN-RcppTN >= 0.2.2
Requires:         R-CRAN-coda >= 0.19.2
Requires:         R-CRAN-Rcpp >= 0.12.19

%description
A suite of functions to estimate, summarize and perform predictions with
the bivariate probit subject to partial observability. The frequentist and
Bayesian probabilistic philosophies are both supported. The frequentist
method is estimated with maximum likelihood and the Bayesian method is
estimated with a Markov Chain Monte Carlo (MCMC) algorithm developed by
Rajbanhdari, A (2014) <doi:10.1002/9781118771051.ch13>.

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
%{rlibdir}/%{packname}/libs
