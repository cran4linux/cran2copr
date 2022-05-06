%global __brp_check_rpaths %{nil}
%global packname  BartMixVs
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Variable Selection Using Bayesian Additive Regression Trees

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-Rcpp >= 1.0.6
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-nnet 
BuildRequires:    R-CRAN-loo 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-CRAN-Rcpp >= 1.0.6
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-nnet 
Requires:         R-CRAN-loo 
Requires:         R-CRAN-mvtnorm 

%description
Bayesian additive regression trees (BART) provides flexible non-parametric
modeling of mixed-type predictors for continuous and binary responses.
This package is built upon CRAN R package 'BART', version 2.7
(<https://github.com/cran/BART>). It implements the three proposed
variable selection approaches in the paper: Luo, C and Daniels, M. J.
(2021), "Variable Selection Using Bayesian Additive Regression Trees."
<arXiv:2112.13998>, and other three existing BART-based variable selection
approaches.

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
