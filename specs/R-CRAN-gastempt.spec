%global packname  gastempt
%global packver   0.4.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.4
Release:          1%{?dist}
Summary:          Analyzing Gastric Emptying from MRI or Scintigraphy

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    make
BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-ggplot2 >= 3.0.0
BuildRequires:    R-CRAN-rstan >= 2.18.1
BuildRequires:    R-CRAN-StanHeaders >= 2.18.0
BuildRequires:    R-CRAN-BH >= 1.66.0.1
BuildRequires:    R-CRAN-rstantools >= 1.5.1
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.4.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.19
BuildRequires:    R-nlme 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-shiny 
Requires:         R-CRAN-ggplot2 >= 3.0.0
Requires:         R-CRAN-rstan >= 2.18.1
Requires:         R-CRAN-rstantools >= 1.5.1
Requires:         R-CRAN-Rcpp >= 0.12.19
Requires:         R-nlme 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-stringr 
Requires:         R-methods 
Requires:         R-CRAN-shiny 

%description
Fits gastric emptying time series from MRI or scintigraphic measurements
using nonlinear mixed-model population fits with 'nlme' and Bayesian
methods with Stan; computes derived parameters such as t50 and AUC.

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
%doc %{rlibdir}/%{packname}/shiny
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
