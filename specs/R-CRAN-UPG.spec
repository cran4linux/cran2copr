%global __brp_check_rpaths %{nil}
%global packname  UPG
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Efficient Bayesian Models for Binary and Categorical Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-mnormt 
BuildRequires:    R-CRAN-pgdraw 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppProgress 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-mnormt 
Requires:         R-CRAN-pgdraw 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-RcppProgress 
Requires:         R-CRAN-coda 

%description
Highly efficient Bayesian implementations of probit, logit, multinomial
logit and binomial logit models. Functions for plotting and tabulating the
estimation output are available as well. Estimation is based on Gibbs
sampling where the Markov chain Monte Carlo algorithms are based on the
latent variable representations and boosting algorithms outlined in
Fr<fc>hwirth-Schnatter S., Zens G., Wagner H. (2020) <arXiv:2011.06898>.
The underlying implementation is written in C++.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
