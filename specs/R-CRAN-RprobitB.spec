%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RprobitB
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Probit Choice Modeling

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-oeli >= 0.7.8
BuildRequires:    R-CRAN-choicedata >= 0.2.0
BuildRequires:    R-CRAN-bayesplot 
BuildRequires:    R-CRAN-bridgesampling 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-CRAN-loo 
BuildRequires:    R-CRAN-posterior 
BuildRequires:    R-CRAN-progressr 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-testthat 
Requires:         R-CRAN-oeli >= 0.7.8
Requires:         R-CRAN-choicedata >= 0.2.0
Requires:         R-CRAN-bayesplot 
Requires:         R-CRAN-bridgesampling 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-future.apply 
Requires:         R-CRAN-loo 
Requires:         R-CRAN-posterior 
Requires:         R-CRAN-progressr 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-Rcpp 
Requires:         R-stats 

%description
Fits Bayesian probit models for binary, multinomial, ordered, and ranked
choices in cross-sectional and panel data. Correlated or uncorrelated
normal and log-normal random coefficients, finite mixtures, sparse finite
mixtures, and Dirichlet process mixtures describe preference
heterogeneity. Multiple Gibbs chains produce posterior draws for
diagnostics and choice prediction. Empirical model data can be supplied as
a data frame or simulated from the requested specification. For an
overarching treatment of the methodology, see Oelschlaeger (2026)
<https://pub.uni-bielefeld.de/record/3014719>. The latent-class model is
described in Oelschlaeger and Bauer (2021)
<https://trid.trb.org/view/1759753>.

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
