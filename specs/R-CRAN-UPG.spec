%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  UPG
%global packver   0.3.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.4
Release:          1%{?dist}%{?buildtag}
Summary:          Efficient Bayesian Algorithms for Binary and Categorical Data Regression Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-mnormt 
BuildRequires:    R-CRAN-pgdraw 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-truncnorm 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-mnormt 
Requires:         R-CRAN-pgdraw 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-truncnorm 

%description
Efficient Bayesian implementations of probit, logit, multinomial logit and
binomial logit models. Functions for plotting and tabulating the
estimation output are available as well. Estimation is based on Gibbs
sampling where the Markov chain Monte Carlo algorithms are based on the
latent variable representations and marginal data augmentation algorithms
described in "Gregor Zens, Sylvia Frühwirth-Schnatter & Helga Wagner
(2023). Ultimate Pólya Gamma Samplers – Efficient MCMC for possibly
imbalanced binary and categorical data, Journal of the American
Statistical Association <doi:10.1080/01621459.2023.2259030>".

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
