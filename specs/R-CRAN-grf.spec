%global packname  grf
%global packver   0.10.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.10.3
Release:          1%{?dist}
Summary:          Generalized Random Forests (Beta)

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    make
BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-sandwich >= 2.4.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.15
BuildRequires:    R-CRAN-DiceKriging 
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-sandwich >= 2.4.0
Requires:         R-CRAN-Rcpp >= 0.12.15
Requires:         R-CRAN-DiceKriging 
Requires:         R-CRAN-lmtest 
Requires:         R-Matrix 
Requires:         R-methods 

%description
A pluggable package for forest-based statistical estimation and inference.
GRF currently provides methods for non-parametric least-squares
regression, quantile regression, and treatment effect estimation
(optionally using instrumental variables). This package is currently in
beta, and we expect to make continual improvements to its performance and
usability.

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
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
