%global packname  BradleyTerryScalable
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Fits the Bradley-Terry Model to Potentially Large and SparseNetworks of Comparison Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-Rcpp >= 0.12.7
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.12.7
Requires:         R-CRAN-igraph 
Requires:         R-Matrix 
Requires:         R-methods 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-dplyr 

%description
Facilities are provided for fitting the simple, unstructured Bradley-Terry
model to networks of binary comparisons. The implemented methods are
designed to scale well to large, potentially sparse, networks. A fairly
high degree of scalability is achieved through the use of EM and MM
algorithms, which are relatively undemanding in terms of memory usage
(relative to some other commonly used methods such as iterative weighted
least squares, for example). Both maximum likelihood and Bayesian MAP
estimation methods are implemented. The package provides various standard
methods for a newly defined 'btfit' model class, such as the extraction
and summarisation of model parameters and the simulation of new datasets
from a fitted model. Tools are also provided for reshaping data into the
newly defined "btdata" class, and for analysing the comparison network,
prior to fitting the Bradley-Terry model. This package complements, rather
than replaces, the existing 'BradleyTerry2' package. (BradleyTerry2 has
rather different aims, which are mainly the specification and fitting of
"structured" Bradley-Terry models in which the strength parameters depend
on covariates.)

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
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
