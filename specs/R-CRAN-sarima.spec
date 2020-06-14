%global packname  sarima
%global packver   0.8.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.2
Release:          2%{?dist}
Summary:          Simulation and Prediction with Seasonal ARIMA Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-PolynomF >= 1.0.0
BuildRequires:    R-CRAN-lagged >= 0.2.1
BuildRequires:    R-CRAN-Rcpp >= 0.12.14
BuildRequires:    R-CRAN-FitAR 
BuildRequires:    R-stats4 
BuildRequires:    R-methods 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-ltsa 
BuildRequires:    R-CRAN-FitARMA 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-KFAS 
BuildRequires:    R-CRAN-FKF 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-PolynomF >= 1.0.0
Requires:         R-CRAN-lagged >= 0.2.1
Requires:         R-CRAN-Rcpp >= 0.12.14
Requires:         R-CRAN-FitAR 
Requires:         R-stats4 
Requires:         R-methods 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-ltsa 
Requires:         R-CRAN-FitARMA 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-KFAS 
Requires:         R-CRAN-FKF 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-dplyr 

%description
Functions, classes and methods for time series modelling with ARIMA and
related models. The aim of the package is to provide consistent interface
for the user. For example, a single function autocorrelations() computes
various kinds of theoretical and sample autocorrelations. This is work in
progress, see the documentation and vignettes for the current
functionality.  Function sarima() fits extended multiplicative seasonal
ARIMA models with trends, exogenous variables and arbitrary roots on the
unit circle, which can be fixed or estimated.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/REFERENCES.bib
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
