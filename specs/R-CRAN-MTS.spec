%global packname  MTS
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}
Summary:          All-Purpose Toolkit for Analyzing Multivariate Time Series (MTS)and Estimating Multivariate Volatility Models

License:          Artistic License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-fGarch 
BuildRequires:    R-CRAN-fBasics 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-fGarch 
Requires:         R-CRAN-fBasics 
Requires:         R-CRAN-mvtnorm 

%description
Multivariate Time Series (MTS) is a general package for analyzing
multivariate linear time series and estimating multivariate volatility
models. It also handles factor models, constrained factor models,
asymptotic principal component analysis commonly used in finance and
econometrics, and principal volatility component analysis.  (a) For the
multivariate linear time series analysis, the package performs model
specification, estimation, model checking, and prediction for many widely
used models, including vector AR models, vector MA models, vector ARMA
models, seasonal vector ARMA models, VAR models with exogenous variables,
multivariate regression models with time series errors, augmented VAR
models, and Error-correction VAR models for co-integrated time series. For
model specification, the package performs structural specification to
overcome the difficulties of identifiability of VARMA models. The methods
used for structural specification include Kronecker indices and Scalar
Component Models.  (b) For multivariate volatility modeling, the MTS
package handles several commonly used models, including multivariate
exponentially weighted moving-average volatility, Cholesky decomposition
volatility models, dynamic conditional correlation (DCC) models,
copula-based volatility models, and low-dimensional BEKK models. The
package also considers multiple tests for conditional heteroscedasticity,
including rank-based statistics.  (c) Finally, the MTS package also
performs forecasting using diffusion index, transfer function analysis,
Bayesian estimation of VAR models, and multivariate time series analysis
with missing values.Users can also use the package to simulate VARMA
models, to compute impulse response functions of a fitted VARMA model, and
to calculate theoretical cross-covariance matrices of a given VARMA model.

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
