%global packname  glarma
%global packver   1.6-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.0
Release:          1%{?dist}
Summary:          Generalized Linear Autoregressive Moving Average Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.3.0
Requires:         R-core >= 2.3.0
BuildArch:        noarch
BuildRequires:    R-MASS 
Requires:         R-MASS 

%description
Functions are provided for estimation, testing, diagnostic checking and
forecasting of generalized linear autoregressive moving average (GLARMA)
models for discrete valued time series with regression variables.  These
are a class of observation driven non-linear non-Gaussian state space
models. The state vector consists of a linear regression component plus an
observation driven component consisting of an autoregressive-moving
average (ARMA) filter of past predictive residuals. Currently three
distributions (Poisson, negative binomial and binomial) can be used for
the response series. Three options (Pearson, score-type and unscaled) for
the residuals in the observation driven component are available.
Estimation is via maximum likelihood (conditional on initializing values
for the ARMA process) optimized using Fisher scoring or Newton Raphson
iterative methods. Likelihood ratio and Wald tests for the observation
driven component allow testing for serial dependence in generalized linear
model settings. Graphical diagnostics including model fits,
autocorrelation functions and probability integral transform residuals are
included in the package. Several standard data sets are included in the
package.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/unitTests
%{rlibdir}/%{packname}/INDEX
