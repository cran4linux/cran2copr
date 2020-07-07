%global packname  icenReg
%global packver   2.0.14
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.14
Release:          3%{?dist}
Summary:          Regression Models for Interval Censored Data

License:          LGPL (>= 2.0, < 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-MLEcens 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-survival 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-foreach 
Requires:         R-methods 
Requires:         R-CRAN-MLEcens 

%description
Regression models for interval censored data. Currently supports Cox-PH,
proportional odds, and accelerated failure time models. Allows for semi
and fully parametric models (parametric only for accelerated failure time
models) and Bayesian parametric models. Includes functions for easy visual
diagnostics of model fits and imputation of censored data.

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
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
