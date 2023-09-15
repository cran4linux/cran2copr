%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pqrBayes
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Penalized Quantile Regression

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-glmnet 

%description
The quantile varying coefficient model is robust to data heterogeneity,
outliers and heavy-tailed distributions in the response variable due to
the check loss function in quantile regression. In addition, it can
flexibly model the dynamic pattern of regression coefficients through
nonparametric varying coefficient functions. Although high dimensional
quantile varying coefficient model has been examined extensively in the
frequentist framework, the corresponding Bayesian variable selection
methods have rarely been developed. In this package, we have implemented
the Gibbs samplers of the penalized Bayesian quantile varying coefficient
model with the spike-and-slab priors [Zhou et
al.(2023)]<doi:10.1016/j.csda.2023.107808>. The Markov Chain Monte Carlo
(MCMC) algorithms of the proposed and alternative models can be
efficiently performed by using the package.

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
