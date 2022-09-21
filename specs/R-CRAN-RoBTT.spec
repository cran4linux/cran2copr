%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RoBTT
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Robust Bayesian T-Test

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-RcppParallel >= 5.0.1
BuildRequires:    R-CRAN-rstan >= 2.21.2
BuildRequires:    R-CRAN-StanHeaders >= 2.18.1
BuildRequires:    R-CRAN-BH >= 1.69.0
BuildRequires:    R-CRAN-rstantools >= 1.5.0
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.4.0
BuildRequires:    R-CRAN-BayesTools >= 0.2.12
BuildRequires:    R-CRAN-Rcpp >= 0.12.19
BuildRequires:    R-CRAN-bridgesampling 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-rstantools
Requires:         R-CRAN-RcppParallel >= 5.0.1
Requires:         R-CRAN-rstan >= 2.21.2
Requires:         R-CRAN-rstantools >= 1.5.0
Requires:         R-CRAN-BayesTools >= 0.2.12
Requires:         R-CRAN-Rcpp >= 0.12.19
Requires:         R-CRAN-bridgesampling 
Requires:         R-methods 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-rstantools

%description
An implementation of Bayesian model-averaged t-test that allows users to
draw inference about the presence vs absence of the effect, heterogeneity
of variances, and outliers. The 'RoBTT' packages estimates model ensembles
of models created as a combination of the competing hypotheses and uses
Bayesian model-averaging to combine the models using posterior model
probabilities. Users can obtain the model-averaged posterior distributions
and inclusion Bayes factors which account for the uncertainty in the data
generating process (Maier et al., 2022, <doi:10.31234/osf.io/d5zwc>).
Users can define a wide range of informative priors for all parameters of
interest. The package provides convenient functions for summary,
visualizations, and fit diagnostics.

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
