%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  frailtypack
%global packver   3.6.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.6.2
Release:          1%{?dist}%{?buildtag}
Summary:          Shared, Joint (Generalized) Frailty Models; Surrogate Endpoints

License:          GPL (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-survC1 
BuildRequires:    R-CRAN-doBy 
BuildRequires:    R-CRAN-statmod 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-rootSolve 
BuildRequires:    R-splines 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-survC1 
Requires:         R-CRAN-doBy 
Requires:         R-CRAN-statmod 
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-rootSolve 
Requires:         R-splines 

%description
The following several classes of frailty models using a penalized
likelihood estimation on the hazard function but also a parametric
estimation can be fit using this R package: 1) A shared frailty model
(with gamma or log-normal frailty distribution) and Cox proportional
hazard model. Clustered and recurrent survival times can be studied. 2)
Additive frailty models for proportional hazard models with two correlated
random effects (intercept random effect with random slope). 3) Nested
frailty models for hierarchically clustered data (with 2 levels of
clustering) by including two iid gamma random effects. 4) Joint frailty
models in the context of the joint modelling for recurrent events with
terminal event for clustered data or not. A joint frailty model for two
semi-competing risks and clustered data is also proposed. 5) Joint general
frailty models in the context of the joint modelling for recurrent events
with terminal event data with two independent frailty terms. 6) Joint
Nested frailty models in the context of the joint modelling for recurrent
events with terminal event, for hierarchically clustered data (with two
levels of clustering) by including two iid gamma random effects. 7)
Multivariate joint frailty models for two types of recurrent events and a
terminal event. 8) Joint models for longitudinal data and a terminal
event. 9) Trivariate joint models for longitudinal data, recurrent events
and a terminal event. 10) Joint frailty models for the validation of
surrogate endpoints in multiple randomized clinical trials with
failure-time and/or longitudinal endpoints with the possibility to use a
mediation analysis model. 11) Conditional and Marginal two-part joint
models for longitudinal semicontinuous data and a terminal event. 12)
Joint frailty-copula models for the validation of surrogate endpoints in
multiple randomized clinical trials with failure-time endpoints. 13)
Generalized shared and joint frailty models for recurrent and terminal
events. Proportional hazards (PH), additive hazard (AH), proportional odds
(PO) and probit models are available in a fully parametric framework. For
PH and AH models, it is possible to consider type-varying coefficients and
flexible semiparametric hazard function. Prediction values are available
(for a terminal event or for a new recurrent event). Left-truncated (not
for Joint model), right-censored data, interval-censored data (only for
Cox proportional hazard and shared frailty model) and strata are allowed.
In each model, the random effects have the gamma or normal distribution.
Now, you can also consider time-varying covariates effects in Cox, shared
and joint frailty models (1-5). The package includes concordance measures
for Cox proportional hazards models and for shared frailty models. 14)
Competing Joint Frailty Model: A single type of recurrent event and two
terminal events. Moreover, the package can be used with its shiny
application, in a local mode or by following the link below.

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
test $(gcc -dumpversion) -ge 10 && mkdir -p ~/.R && echo "FFLAGS=$(R CMD config FFLAGS) -fallow-argument-mismatch" > ~/.R/Makevars
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
