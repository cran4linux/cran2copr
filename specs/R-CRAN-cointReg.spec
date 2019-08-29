%global packname  cointReg
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}
Summary:          Parameter Estimation and Inference in a Cointegrating Regression

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-checkmate >= 1.6.0
BuildRequires:    R-CRAN-matrixStats >= 0.14.1
BuildRequires:    R-MASS 
Requires:         R-CRAN-checkmate >= 1.6.0
Requires:         R-CRAN-matrixStats >= 0.14.1
Requires:         R-MASS 

%description
Cointegration methods are widely used in empirical macroeconomics and
empirical finance. It is well known that in a cointegrating regression the
ordinary least squares (OLS) estimator of the parameters is
super-consistent, i.e. converges at rate equal to the sample size T. When
the regressors are endogenous, the limiting distribution of the OLS
estimator is contaminated by so-called second order bias terms, see e.g.
Phillips and Hansen (1990) <DOI:10.2307/2297545>. The presence of these
bias terms renders inference difficult. Consequently, several
modifications to OLS that lead to zero mean Gaussian mixture limiting
distributions have been proposed, which in turn make standard asymptotic
inference feasible. These methods include the fully modified OLS (FM-OLS)
approach of Phillips and Hansen (1990) <DOI:10.2307/2297545>, the dynamic
OLS (D-OLS) approach of Phillips and Loretan (1991) <DOI:10.2307/2298004>,
Saikkonen (1991) <DOI:10.1017/S0266466600004217> and Stock and Watson
(1993) <DOI:10.2307/2951763> and the new estimation approach called
integrated modified OLS (IM-OLS) of Vogelsang and Wagner (2014)
<DOI:10.1016/j.jeconom.2013.10.015>. The latter is based on an augmented
partial sum (integration) transformation of the regression model. IM-OLS
is similar in spirit to the FM- and D-OLS approaches, with the key
difference that it does not require estimation of long run variance
matrices and avoids the need to choose tuning parameters (kernels,
bandwidths, lags). However, inference does require that a long run
variance be scaled out. This package provides functions for the parameter
estimation and inference with all three modified OLS approaches. That
includes the automatic bandwidth selection approaches of Andrews (1991)
<DOI:10.2307/2938229> and of Newey and West (1994) <DOI:10.2307/2297912>
as well as the calculation of the long run variance.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/INDEX
