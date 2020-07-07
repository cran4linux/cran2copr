%global packname  ergmito
%global packver   0.2-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          3%{?dist}
Summary:          Exponential Random Graph Models for Small Networks

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-ergm 
BuildRequires:    R-CRAN-network 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-texreg 
BuildRequires:    R-stats 
BuildRequires:    R-parallel 
BuildRequires:    R-utils 
BuildRequires:    R-methods 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-ergm 
Requires:         R-CRAN-network 
Requires:         R-MASS 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-texreg 
Requires:         R-stats 
Requires:         R-parallel 
Requires:         R-utils 
Requires:         R-methods 
Requires:         R-graphics 

%description
Simulation and estimation of Exponential Random Graph Models (ERGMs) for
small networks using exact statistics. As a difference from the 'ergm'
package, 'ergmito' circumvents using Markov-Chain Maximum Likelihood
Estimator (MC-MLE) and instead uses Maximum Likelihood Estimator (MLE) to
fit ERGMs for small networks. As exhaustive enumeration is computationally
feasible for small networks, this R package takes advantage of this and
provides tools for calculating likelihood functions, and other relevant
functions, directly, meaning that in many cases both estimation and
simulation of ERGMs for small networks can be faster and more accurate
than simulation-based algorithms.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/test-data-for-tests.R
%{rlibdir}/%{packname}/test-data-for-tests.rda
%doc %{rlibdir}/%{packname}/tinytest
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
