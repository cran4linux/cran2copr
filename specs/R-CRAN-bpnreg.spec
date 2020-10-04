%global packname  bpnreg
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          3%{?dist}%{?buildtag}
Summary:          Bayesian Projected Normal Regression Models for Circular Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildRequires:    R-MASS >= 7.3.51.4
BuildRequires:    R-methods >= 3.6.0
BuildRequires:    R-CRAN-haven >= 2.1.1
BuildRequires:    R-CRAN-BH >= 1.69.0.1
BuildRequires:    R-CRAN-Rcpp >= 1.0.2
BuildRequires:    R-CRAN-RcppArmadillo >= 0.9.800.1.0
Requires:         R-MASS >= 7.3.51.4
Requires:         R-methods >= 3.6.0
Requires:         R-CRAN-haven >= 2.1.1
Requires:         R-CRAN-Rcpp >= 1.0.2

%description
Fitting Bayesian multiple and mixed-effect regression models for circular
data based on the projected normal distribution. Both continuous and
categorical predictors can be included. Sampling from the posterior is
performed via an MCMC algorithm. Posterior descriptives of all parameters,
model fit statistics and Bayes factors for hypothesis tests for inequality
constrained hypotheses are provided. See Cremers, Mulder & Klugkist (2018)
<doi:10.1111/bmsp.12108> and Nuñez-Antonio & Guttiérez-Peña (2014)
<doi:10.1016/j.csda.2012.07.025>.

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
