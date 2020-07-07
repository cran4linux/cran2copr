%global packname  bayesdfa
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          3%{?dist}
Summary:          Bayesian Dynamic Factor Analysis (DFA) with 'Stan'

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    make
BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-rstan >= 2.18.2
BuildRequires:    R-CRAN-StanHeaders >= 2.18.1
BuildRequires:    R-CRAN-loo >= 2.0.0
BuildRequires:    R-CRAN-BH >= 1.66.0
BuildRequires:    R-CRAN-rstantools >= 1.5.1
BuildRequires:    R-CRAN-dplyr >= 0.8.0
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.3.0
BuildRequires:    R-CRAN-rlang >= 0.3.1
BuildRequires:    R-CRAN-Rcpp >= 0.12.8
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-reshape2 
Requires:         R-CRAN-rstan >= 2.18.2
Requires:         R-CRAN-loo >= 2.0.0
Requires:         R-CRAN-rstantools >= 1.5.1
Requires:         R-CRAN-dplyr >= 0.8.0
Requires:         R-CRAN-rlang >= 0.3.1
Requires:         R-CRAN-Rcpp >= 0.12.8
Requires:         R-methods 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-reshape2 

%description
Implements Bayesian dynamic factor analysis with 'Stan'. Dynamic factor
analysis is a dimension reduction tool for multivariate time series.
'bayesdfa' extends conventional dynamic factor models in several ways.
First, extreme events may be estimated in the latent trend by modeling
process error with a student-t distribution. Second, autoregressive and
moving average components can be optionally included. Third, the estimated
dynamic factors can be analyzed with hidden Markov models to evaluate
support for latent regimes.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/include
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
