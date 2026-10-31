%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BayesianQDM
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Quantitative Decision-Making Framework for Binary, Continuous and Time-to-Event Endpoints

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-stats 
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-grDevices 
Requires:         R-CRAN-Rcpp 
Requires:         R-stats 

%description
Bayesian quantitative decision-making for proof-of-concept clinical trials
with Go, NoGo and Gray decisions. A study is specified by its sample
sizes, conjugate prior distributions, external data borrowed through power
priors, a concurrent, external, hypothetical or fixed control group, and a
decision criterion based on the posterior or posterior predictive
probability of the treatment effect. The package computes the decision for
observed data, the operating characteristics of a design under scenarios
for the true parameters, the decision thresholds that control the
probabilities of false Go and false NoGo decisions, and the observed data
that lead to each decision. One or two binary endpoints (Beta-binomial and
Dirichlet-multinomial models), one or two continuous endpoints
(Normal-Inverse-chi-squared and Normal-Inverse-Wishart models) and one
time-to-event endpoint evaluated by the milestone survival probability or
the hazard ratio (exponential model with Gamma priors) are supported, with
larger or smaller effects as favorable. The posterior distributions have
closed forms, so Markov chain Monte Carlo (MCMC) sampling is not needed;
the probabilities are computed from closed-form distribution functions, by
exact summation, numerical integration, a moment-matching approximation or
Monte Carlo simulation, with the main computations in C++. See Kang,
Yamaguchi, and Han (2026) <doi:10.1080/10543406.2026.2655410> for the
methodological framework.

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
