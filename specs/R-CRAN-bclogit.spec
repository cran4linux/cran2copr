%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bclogit
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Conditional Logistic Regression

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildRequires:    R-CRAN-RcppParallel >= 5.0.1
BuildRequires:    R-CRAN-rstantools >= 2.6.0
BuildRequires:    R-CRAN-rstan >= 2.18.1
BuildRequires:    R-CRAN-StanHeaders >= 2.18.0
BuildRequires:    R-CRAN-BH >= 1.66.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.14
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.3.0
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-fastLogisticRegressionWrap 
BuildRequires:    R-CRAN-geepack 
BuildRequires:    R-CRAN-glmmTMB 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rstantools
Requires:         R-CRAN-RcppParallel >= 5.0.1
Requires:         R-CRAN-rstantools >= 2.6.0
Requires:         R-CRAN-rstan >= 2.18.1
Requires:         R-CRAN-Rcpp >= 1.0.14
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-fastLogisticRegressionWrap 
Requires:         R-CRAN-geepack 
Requires:         R-CRAN-glmmTMB 
Requires:         R-methods 
Requires:         R-CRAN-rstantools

%description
Performs inference for Bayesian conditional logistic regression with
informative priors built from the concordant pair data. We include many
options to build the priors. And we include many options during the
inference step for estimation, testing and confidence set creation. For
details, see Kapelner and Tennenbaum (2026) ``Improved Conditional
Logistic Regression using Information in Concordant Pairs with Software''
<doi:10.48550/arXiv.2602.08212>.

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
