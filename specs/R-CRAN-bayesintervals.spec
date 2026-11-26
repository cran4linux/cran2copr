%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bayesintervals
%global packver   3.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Reducible Imprecision and Bayesian Intervals for Mixed Models

License:          Apache License (== 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-bslib 
BuildRequires:    R-CRAN-later 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-bslib 
Requires:         R-CRAN-later 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-plotly 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-grDevices 

%description
Calculates and visualizes Bayesian credible, prediction and tolerance
intervals, and posterior predictive distributions, for linear mixed models
from Markov chain Monte Carlo (MCMC) samples of the model parameters.
Users define the model through fixed effects, variance components and
optional covariates, and results can be back-transformed from the log
scale. Tolerance intervals are derived from the posterior predictive
distribution following Krishnamoorthy and Mathew (2009)
<doi:10.1002/9780470473900>, including the construction of one-dimensional
two-sided intervals from the bivariate posterior of the lower and upper
quantiles. Reducible imprecision measures the share of the
tolerance-interval half-width that exceeds the prediction-interval
half-width, that is, the epistemic uncertainty that more data could
reduce. The package includes an interactive 'shiny' application, started
with start_app_view(), which has its own name: 'BSI' (Bayesian Statistical
Intervals). The development repository on 'GitHub' is called
'BayesianSI.Calculator'.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
