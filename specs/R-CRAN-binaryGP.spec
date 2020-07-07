%global packname  binaryGP
%global packver   0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2
Release:          3%{?dist}
Summary:          Fit and Predict a Gaussian Process Model with (Time-Series)Binary Response

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.1
Requires:         R-core >= 2.14.1
BuildRequires:    R-CRAN-nloptr >= 1.0.4
BuildRequires:    R-CRAN-GPfit >= 1.0.0
BuildRequires:    R-CRAN-logitnorm >= 0.8.29
BuildRequires:    R-CRAN-Rcpp >= 0.12.0
BuildRequires:    R-CRAN-lhs >= 0.10
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-nloptr >= 1.0.4
Requires:         R-CRAN-GPfit >= 1.0.0
Requires:         R-CRAN-logitnorm >= 0.8.29
Requires:         R-CRAN-Rcpp >= 0.12.0
Requires:         R-CRAN-lhs >= 0.10
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-utils 
Requires:         R-methods 

%description
Allows the estimation and prediction for binary Gaussian process model.
The mean function can be assumed to have time-series structure. The
estimation methods for the unknown parameters are based on penalized
quasi-likelihood/penalized quasi-partial likelihood and restricted maximum
likelihood. The predicted probability and its confidence interval are
computed by Metropolis-Hastings algorithm. More details can be seen in
Sung et al (2017) <arXiv:1705.02511>.

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
