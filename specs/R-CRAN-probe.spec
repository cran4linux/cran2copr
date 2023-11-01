%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  probe
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Sparse High-Dimensional Linear Regression with PROBE

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.00
Requires:         R-core >= 4.00
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-glmnet 

%description
Implements an efficient and powerful Bayesian approach for sparse
high-dimensional linear regression. It uses minimal prior assumptions on
the parameters through plug-in empirical Bayes estimates of
hyperparameters. An efficient Parameter-Expanded
Expectation-Conditional-Maximization (PX-ECM) algorithm estimates maximum
a posteriori (MAP) values of regression parameters and variable selection
probabilities. The PX-ECM results in a robust computationally efficient
coordinate-wise optimization, which adjusts for the impact of other
predictor variables. The E-step is motivated by the popular two-group
approach to multiple testing. The result is a PaRtitiOned empirical Bayes
Ecm (PROBE) algorithm applied to sparse high-dimensional linear
regression, implemented using one-at-a-time or all-at-once type
optimization. More information can be found in McLain, Zgodic, and Bondell
(2022) <arXiv:2209.08139>.

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
