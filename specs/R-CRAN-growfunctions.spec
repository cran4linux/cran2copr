%global packname  growfunctions
%global packver   0.14
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.14
Release:          3%{?dist}
Summary:          Bayesian Non-Parametric Dependent Models for Time-IndexedFunctional Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.2
Requires:         R-core >= 3.2.2
BuildRequires:    R-CRAN-reshape2 >= 1.2.2
BuildRequires:    R-CRAN-ggplot2 >= 1.0.1
BuildRequires:    R-CRAN-mvtnorm >= 1.0.0
BuildRequires:    R-CRAN-RcppArmadillo >= 0.8.400.0.0
BuildRequires:    R-CRAN-spam >= 0.41.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.16
Requires:         R-CRAN-reshape2 >= 1.2.2
Requires:         R-CRAN-ggplot2 >= 1.0.1
Requires:         R-CRAN-mvtnorm >= 1.0.0
Requires:         R-CRAN-spam >= 0.41.0
Requires:         R-CRAN-Rcpp >= 0.12.16

%description
Estimates a collection of time-indexed functions under either of Gaussian
process (GP) or intrinsic Gaussian Markov random field (iGMRF) prior
formulations where a Dirichlet process mixture allows sub-groupings of the
functions to share the same covariance or precision parameters.  The GP
and iGMRF formulations both support any number of additive covariance or
precision terms, respectively, expressing either or both of multiple trend
and seasonality.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
