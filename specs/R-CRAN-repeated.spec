%global __brp_check_rpaths %{nil}
%global packname  repeated
%global packver   1.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.2
Release:          3%{?dist}%{?buildtag}
Summary:          Non-Normal Repeated Measurements Models

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 1.4
Requires:         R-core >= 1.4
BuildRequires:    R-CRAN-rmutil 
Requires:         R-CRAN-rmutil 

%description
Various functions to fit models for non-normal repeated measurements, such
as Binary Random Effects Models with Two Levels of Nesting, Bivariate
Beta-binomial Regression Models, Marginal Bivariate Binomial Regression
Models, Cormack capture-recapture models, Continuous-time Hidden Markov
Chain Models, Discrete-time Hidden Markov Chain Models, Changepoint
Location Models using a Continuous-time Two-state Hidden Markov Chain,
generalized nonlinear autoregression models, multivariate Gaussian copula
models, generalized non-linear mixed models with one random effect,
generalized non-linear mixed models using h-likelihood for one random
effect, Repeated Measurements Models for Counts with Frailty or Serial
Dependence, Repeated Measurements Models for Continuous Variables with
Frailty or Serial Dependence, Ordinal Random Effects Models with Dropouts,
marginal homogeneity models for square contingency tables, correlated
negative binomial models with Kalman update. References include Lindey's
text books, JK Lindsey (2001) <isbn-10:0198508123> and JK Lindsey (1999)
<isbn-10:0198505590>.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
