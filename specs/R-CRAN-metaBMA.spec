%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  metaBMA
%global packver   0.6.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.9
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Model Averaging for Random and Fixed Effects Meta-Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-RcppParallel >= 5.0.1
BuildRequires:    R-CRAN-rstantools >= 2.3.0
BuildRequires:    R-CRAN-rstan >= 2.26.0
BuildRequires:    R-CRAN-StanHeaders >= 2.26.0
BuildRequires:    R-CRAN-BH >= 1.78.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.0
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.9.1
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-bridgesampling 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-LaplacesDemon 
BuildRequires:    R-CRAN-logspline 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-rstantools
Requires:         R-CRAN-RcppParallel >= 5.0.1
Requires:         R-CRAN-rstantools >= 2.3.0
Requires:         R-CRAN-rstan >= 2.26.0
Requires:         R-CRAN-Rcpp >= 1.0.0
Requires:         R-methods 
Requires:         R-CRAN-bridgesampling 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-LaplacesDemon 
Requires:         R-CRAN-logspline 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-rstantools

%description
Computes the posterior model probabilities for standard meta-analysis
models (null model vs. alternative model assuming either fixed- or
random-effects, respectively). These posterior probabilities are used to
estimate the overall mean effect size as the weighted average of the mean
effect size estimates of the random- and fixed-effect model as proposed by
Gronau, Van Erp, Heck, Cesario, Jonas, & Wagenmakers (2017,
<doi:10.1080/23743603.2017.1326760>). The user can define a wide range of
non-informative or informative priors for the mean effect size and the
heterogeneity coefficient. Moreover, using pre-compiled Stan models,
meta-analysis with continuous and discrete moderators with
Jeffreys-Zellner-Siow (JZS) priors can be fitted and tested. This allows
to compute Bayes factors and perform Bayesian model averaging across
random- and fixed-effects meta-analysis with and without moderators. For a
primer on Bayesian model-averaged meta-analysis, see Gronau, Heck,
Berkhout, Haaf, & Wagenmakers (2021, <doi:10.1177/25152459211031256>).

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
