%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  emBayes
%global packver   0.1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.6
Release:          1%{?dist}%{?buildtag}
Summary:          Robust Bayesian Variable Selection via Expectation-Maximization

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-glmnet 

%description
Variable selection methods have been extensively developed for analyzing
highdimensional omics data within both the frequentist and Bayesian
frameworks. This package provides implementations of the spike-and-slab
quantile (group) LASSO which have been developed along the line of
Bayesian hierarchical models but deeply rooted in frequentist
regularization methods by utilizing Expectation–Maximization (EM)
algorithm. The spike-and-slab quantile LASSO can handle data irregularity
in terms of skewness and outliers in response variables, compared to its
non-robust alternative, the spike-and-slab LASSO, which has also been
implemented in the package. In addition, procedures for fitting the
spike-and-slab quantile group LASSO and its non-robust counterpart have
been implemented in the form of quantile/least-square varying coefficient
mixed effect models for high-dimensional longitudinal data. The core
module of this package is developed in 'C++'.

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
