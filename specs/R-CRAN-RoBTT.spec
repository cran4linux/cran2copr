%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RoBTT
%global packver   1.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Robust Bayesian T-Test

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-RcppParallel >= 5.0.1
BuildRequires:    R-CRAN-rstan >= 2.26.0
BuildRequires:    R-CRAN-StanHeaders >= 2.26.0
BuildRequires:    R-CRAN-BH >= 1.69.0
BuildRequires:    R-CRAN-rstantools >= 1.5.0
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.4.0
BuildRequires:    R-CRAN-BayesTools >= 0.2.15
BuildRequires:    R-CRAN-Rcpp >= 0.12.19
BuildRequires:    R-CRAN-bridgesampling 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-rstantools
Requires:         R-CRAN-RcppParallel >= 5.0.1
Requires:         R-CRAN-rstan >= 2.26.0
Requires:         R-CRAN-rstantools >= 1.5.0
Requires:         R-CRAN-BayesTools >= 0.2.15
Requires:         R-CRAN-Rcpp >= 0.12.19
Requires:         R-CRAN-bridgesampling 
Requires:         R-methods 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-rstantools

%description
An implementation of Bayesian model-averaged t-tests that allows users to
draw inferences about the presence versus absence of an effect, variance
heterogeneity, and potential outliers. The 'RoBTT' package estimates
ensembles of models created by combining competing hypotheses and applies
Bayesian model averaging using posterior model probabilities. Users can
obtain model-averaged posterior distributions and inclusion Bayes factors,
accounting for uncertainty in the data-generating process (Maier et al.,
2024, <doi:10.3758/s13423-024-02590-5>). The package also provides a
truncated likelihood version of the model-averaged t-test, enabling users
to exclude potential outliers without introducing bias (Godmann et al.,
2024, <doi:10.31234/osf.io/j9f3s>). Users can specify a wide range of
informative priors for all parameters of interest. The package offers
convenient functions for summary, visualization, and fit diagnostics.

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
