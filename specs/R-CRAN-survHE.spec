%global packname  survHE
%global packver   1.0.65
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.65
Release:          1%{?dist}
Summary:          Survival Analysis in Health Economic Evaluation

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    make
BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-rstan >= 2.18.1
BuildRequires:    R-CRAN-StanHeaders >= 2.18.0
BuildRequires:    R-CRAN-BH >= 1.66.0.1
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.4.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.19
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-flexsurv 
BuildRequires:    R-CRAN-rms 
BuildRequires:    R-CRAN-xlsx 
BuildRequires:    R-tools 
Requires:         R-CRAN-rstan >= 2.18.1
Requires:         R-CRAN-Rcpp >= 0.12.19
Requires:         R-methods 
Requires:         R-CRAN-flexsurv 
Requires:         R-CRAN-rms 
Requires:         R-CRAN-xlsx 
Requires:         R-tools 

%description
Contains a suite of functions for survival analysis in health economics.
These can be used to run survival models under a frequentist (based on
maximum likelihood) or a Bayesian approach (both based on Integrated
Nested Laplace Approximation or Hamiltonian Monte Carlo). The user can
specify a set of parametric models using a common notation and select the
preferred mode of inference. The results can also be post-processed to
produce probabilistic sensitivity analysis and can be used to export the
output to an Excel file (e.g. for a Markov model, as often done by
modellers and practitioners).

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/include
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
