%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pumBayes
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Estimation of Probit Unfolding Models for Binary Preference Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-RcppDist 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-RcppTN 
Requires:         R-CRAN-Rcpp 

%description
Bayesian estimation and analysis methods for Probit Unfolding Models
(PUMs), a novel class of scaling models designed for binary preference
data. These models allow for both monotonic and non-monotonic response
functions. The package supports Bayesian inference for both static and
dynamic PUMs using Markov chain Monte Carlo (MCMC) algorithms with minimal
or no tuning. Key functionalities include posterior sampling,
hyperparameter selection, data preprocessing, model fit evaluation, and
visualization. The methods are particularly suited to analyzing voting
data, such as from the U.S. Congress or Supreme Court, but can also be
applied in other contexts where non-monotonic responses are expected. For
methodological details, see Shi et al. (2025)
<doi:10.48550/arXiv.2504.00423>.

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
