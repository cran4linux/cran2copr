%global packname  NHMM
%global packver   3.10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.10
Release:          2%{?dist}
Summary:          Bayesian Non-Homogeneous Markov and Mixture Models for MultipleTime Series

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.11.0
BuildRequires:    R-CRAN-BayesLogit 
BuildRequires:    R-CRAN-msm 
BuildRequires:    R-CRAN-MCMCpack 
BuildRequires:    R-MASS 
Requires:         R-CRAN-Rcpp >= 0.11.0
Requires:         R-CRAN-BayesLogit 
Requires:         R-CRAN-msm 
Requires:         R-CRAN-MCMCpack 
Requires:         R-MASS 

%description
Holsclaw, Greene, Robertson, and Smyth (2017) <doi:10.1214/16-AOAS1009>.
Bayesian HMM and NHMM modeling for multiple time series. The emission
distribution can be mixtures of Exponential, Gamma, Poisson, or Normal
distributions, and zero inflation is possible.

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
