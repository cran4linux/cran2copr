%global packname  dfpk
%global packver   3.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.5.1
Release:          3%{?dist}%{?buildtag}
Summary:          Bayesian Dose-Finding Designs using Pharmacokinetics (PK) forPhase I Clinical Trials

License:          GPL (>= 3) | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    make
BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-rstan >= 2.18.1
BuildRequires:    R-CRAN-StanHeaders >= 2.18.0
BuildRequires:    R-CRAN-ggplot2 >= 2.0.0
BuildRequires:    R-CRAN-BH >= 1.66
BuildRequires:    R-CRAN-Rcpp >= 0.12.11
BuildRequires:    R-CRAN-dfcrm 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-PK 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-rstan >= 2.18.1
Requires:         R-CRAN-ggplot2 >= 2.0.0
Requires:         R-CRAN-Rcpp >= 0.12.11
Requires:         R-CRAN-dfcrm 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-PK 

%description
Statistical methods involving PK measures are provided, in the dose
allocation process during a Phase I clinical trials. These methods,
proposed by Ursino et al, (2017) <doi:10.1002/bimj.201600084>, enter
pharmacokinetics (PK) in the dose finding designs in different ways,
including covariates models, dependent variable or hierarchical models.
This package provides functions to generate data from several scenarios
and functions to run simulations which their objective is to determine the
maximum tolerated dose (MTD).

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
%doc %{rlibdir}/%{packname}/exec
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/chunks
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
