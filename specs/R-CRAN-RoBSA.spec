%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RoBSA
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Robust Bayesian Survival Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    jags-devel
BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-BayesTools >= 0.2.14
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-rjags 
BuildRequires:    R-CRAN-runjags 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-Rdpack 
Requires:         R-CRAN-BayesTools >= 0.2.14
Requires:         R-CRAN-survival 
Requires:         R-CRAN-rjags 
Requires:         R-CRAN-runjags 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-coda 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-Rdpack 

%description
A framework for estimating ensembles of parametric survival models with
different parametric families. The RoBSA framework uses Bayesian
model-averaging to combine the competing parametric survival models into a
model ensemble, weights the posterior parameter distributions based on
posterior model probabilities and uses Bayes factors to test for the
presence or absence of the individual predictors or preference for a
parametric family (Bartoš, Aust & Haaf, 2022,
<doi:10.1186/s12874-022-01676-9>). The user can define a wide range of
informative priors for all parameters of interest. The package provides
convenient functions for summary, visualizations, fit diagnostics, and
prior distribution calibration.

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
