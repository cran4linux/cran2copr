%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PEPBVS
%global packver   2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Variable Selection using Power-Expected-Posterior Prior

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-Rcpp >= 1.0.9
BuildRequires:    R-CRAN-BAS 
BuildRequires:    R-CRAN-BayesVarSel 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-mcmcse 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-RcppGSL 
Requires:         R-CRAN-Rcpp >= 1.0.9
Requires:         R-CRAN-BAS 
Requires:         R-CRAN-BayesVarSel 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-mcmcse 
Requires:         R-CRAN-mvtnorm 

%description
Performs Bayesian variable selection under normal linear models for the
data with the model parameters following as prior distributions either the
power-expected-posterior (PEP) or the intrinsic (a special case of the
former) (Fouskakis and Ntzoufras (2022) <doi: 10.1214/21-BA1288>,
Fouskakis and Ntzoufras (2020) <doi: 10.3390/econometrics8020017>). The
prior distribution on model space is the uniform over all models or the
uniform on model dimension (a special case of the beta-binomial prior).
The selection is performed by either implementing a full enumeration and
evaluation of all possible models or using the Markov Chain Monte Carlo
Model Composition (MC3) algorithm (Madigan and York (1995) <doi:
10.2307/1403615>). Complementary functions for hypothesis testing,
estimation and predictions under Bayesian model averaging, as well as,
plotting and printing the results are also provided. The results can be
compared to the ones obtained under other well-known priors on model
parameters and model spaces.

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
