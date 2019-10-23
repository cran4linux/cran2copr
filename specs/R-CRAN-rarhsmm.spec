%global packname  rarhsmm
%global packver   1.0.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.7
Release:          1%{?dist}
Summary:          Regularized Autoregressive Hidden Semi Markov Model

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.9
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.12.9
Requires:         R-CRAN-glmnet 

%description
Fit Gaussian hidden Markov (or semi-Markov) models with / without
autoregressive coefficients and with / without regularization. The fitting
algorithm for the hidden Markov model is illustrated by Rabiner (1989)
<doi:10.1109/5.18626>. The shrinkage estimation on the covariance matrices
is based on the method by Ledoit et al. (2004)
<doi:10.1016/S0047-259X(03)00096-4>. The shrinkage estimation on the
autoregressive coefficients uses the elastic net shrinkage detailed in Zou
et al. (2005) <doi:10.1111/j.1467-9868.2005.00503.x>.

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
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
