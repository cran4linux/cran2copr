%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pqrBayes
%global packver   1.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.5
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Penalized Quantile Regression

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-splines 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-glmnet 
Requires:         R-splines 
Requires:         R-stats 

%description
The quantile varying coefficient model is robust to data heterogeneity,
outliers and heavy-tailed distributions in the response variable. In
addition, it can flexibly model dynamic patterns of regression
coefficients through nonparametric varying coefficient functions. In this
package, we have implemented the Gibbs samplers of the penalized Bayesian
quantile varying coefficient model with spike-and-slab priors [Zhou et
al.(2023)]<doi:10.1016/j.csda.2023.107808> for efficient Bayesian
shrinkage estimation, variable selection and statistical inference. In
particular, valid Bayesian inferences on sparse quantile varying
coefficient functions can be validated on finite samples. The Markov Chain
Monte Carlo (MCMC) algorithms of the proposed and alternative models can
be efficiently performed by using the package.

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
