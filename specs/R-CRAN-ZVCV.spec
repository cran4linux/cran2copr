%global packname  ZVCV
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          Zero-Variance Control Variates

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.11.0
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-partitions 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.11.0
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-partitions 
Requires:         R-stats 

%description
Zero-variance control variates (ZV-CV, Mira et al. (2013)
<doi:10.1007/s11222-012-9344-6>) is a post-processing method to reduce the
variance of Monte Carlo estimators of expectations using the derivatives
of the log target. Once the derivatives are available, the only additional
computational effort is in solving a linear regression problem. Recently,
this method has been extended to higher dimensions using regularisation
(South et al., 2018 <arXiv:1811.05073>). This package can be used to
easily perform ZV-CV or regularised ZV-CV when a set of samples,
derivatives and function evaluations are available. Additional functions
for applying ZV-CV to two estimators for the normalising constant of the
posterior distribution in Bayesian statistics are also supplied.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
