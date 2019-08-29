%global packname  ctmcd
%global packver   1.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.1
Release:          1%{?dist}
Summary:          Estimating the Parameters of a Continuous-Time Markov Chain fromDiscrete-Time Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.12.17
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-expm 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.12.17
Requires:         R-CRAN-coda 
Requires:         R-CRAN-expm 
Requires:         R-CRAN-numDeriv 

%description
Functions for estimating Markov generator matrices from discrete-time
observations. The implemented approaches comprise diagonal adjustment,
weighted adjustment and quasi-optimization of matrix logarithm based
candidate solutions, an expectation-maximization algorithm as well as a
Gibbs sampler.

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
%{rlibdir}/%{packname}/include
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
