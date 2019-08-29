%global packname  carfima
%global packver   2.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.1
Release:          1%{?dist}
Summary:          Continuous-Time Fractionally Integrated ARMA Process forIrregularly Spaced Long-Memory Time Series Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-DEoptim 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-cubature 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-truncnorm 
BuildRequires:    R-CRAN-invgamma 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-DEoptim 
Requires:         R-CRAN-Rdpack 
Requires:         R-MASS 
Requires:         R-CRAN-cubature 
Requires:         R-CRAN-numDeriv 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-truncnorm 
Requires:         R-CRAN-invgamma 

%description
We provide a toolbox to fit a continuous-time fractionally integrated ARMA
process (CARFIMA) on univariate and irregularly spaced time series data
via frequentist or Bayesian machinery. A general-order CARFIMA(p, H, q)
model for p>q is specified in Tsai and Chan (2005)
<doi:10.1111/j.1467-9868.2005.00522.x> and it involves (p+q+2) unknown
model parameters, i.e., p AR parameters, q MA parameters, Hurst parameter
H, and process uncertainty (standard deviation) sigma. The package
produces their maximum likelihood estimates and asymptotic uncertainties
using a global optimizer called the differential evolution algorithm. It
also produces their posterior distributions via Metropolis within a Gibbs
sampler equipped with adaptive Markov chain Monte Carlo for posterior
sampling. These fitting procedures, however, may produce numerical errors
if p>2. The toolbox also contains a function to simulate discrete time
series data from CARFIMA(p, H, q) process given the model parameters and
observation times.

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
%doc %{rlibdir}/%{packname}/REFERENCES.bib
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
