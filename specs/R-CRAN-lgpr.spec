%global __brp_check_rpaths %{nil}
%global packname  lgpr
%global packver   1.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.5
Release:          1%{?dist}%{?buildtag}
Summary:          Longitudinal Gaussian Process Regression

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-MASS >= 7.3.50
BuildRequires:    R-CRAN-RcppParallel >= 5.0.2
BuildRequires:    R-stats >= 3.4
BuildRequires:    R-CRAN-ggplot2 >= 3.1.0
BuildRequires:    R-CRAN-rstan >= 2.21.2
BuildRequires:    R-CRAN-StanHeaders >= 2.21.0.7
BuildRequires:    R-CRAN-rstantools >= 2.1.1
BuildRequires:    R-CRAN-RCurl >= 1.98
BuildRequires:    R-CRAN-BH >= 1.75.0.0
BuildRequires:    R-CRAN-bayesplot >= 1.7.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.6
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.9.1
BuildRequires:    R-CRAN-gridExtra >= 0.3
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rstantools
Requires:         R-CRAN-MASS >= 7.3.50
Requires:         R-CRAN-RcppParallel >= 5.0.2
Requires:         R-stats >= 3.4
Requires:         R-CRAN-ggplot2 >= 3.1.0
Requires:         R-CRAN-rstan >= 2.21.2
Requires:         R-CRAN-rstantools >= 2.1.1
Requires:         R-CRAN-RCurl >= 1.98
Requires:         R-CRAN-bayesplot >= 1.7.0
Requires:         R-CRAN-gridExtra >= 0.3
Requires:         R-CRAN-Rcpp >= 1.0.6
Requires:         R-methods 
Requires:         R-CRAN-rstantools

%description
Interpretable nonparametric modeling of longitudinal data using additive
Gaussian process regression. Contains functionality for inferring
covariate effects and assessing covariate relevances. Models are specified
using a convenient formula syntax, and can include shared, group-specific,
non-stationary, heterogeneous and temporally uncertain effects. Bayesian
inference for model parameters is performed using 'Stan'. The modeling
approach and methods are described in detail in Timonen et al. (2021)
<doi:10.1093/bioinformatics/btab021>.

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
