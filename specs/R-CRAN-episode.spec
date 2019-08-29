%global packname  episode
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          Estimation with Penalisation in Systems of Ordinary DifferentialEquations

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    make
BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-methods >= 3.4
BuildRequires:    R-stats >= 3.4
BuildRequires:    R-CRAN-glmnet >= 2.0.10
BuildRequires:    R-CRAN-nnls >= 1.4
BuildRequires:    R-Matrix >= 1.2.9
BuildRequires:    R-CRAN-Rcpp >= 0.12.11
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-methods >= 3.4
Requires:         R-stats >= 3.4
Requires:         R-CRAN-glmnet >= 2.0.10
Requires:         R-CRAN-nnls >= 1.4
Requires:         R-Matrix >= 1.2.9
Requires:         R-CRAN-Rcpp >= 0.12.11

%description
A set of statistical tools for inferring unknown parameters in continuous
time processes governed by ordinary differential equations (ODE).
Moreover, variance reduction and model selection can be obtained through
various implemented penalisation schemes. The package offers two
estimation procedures: exact estimation via least squares and a faster
approximate estimation via inverse collocation methods. All estimators can
handle multiple data sets arising from the same ODE system, but subjected
to different interventions.

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
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
