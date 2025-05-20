%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  densityratio
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Distribution Comparison Through Density Ratio Estimation

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-osqp 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-RcppProgress 
Requires:         R-CRAN-osqp 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-ggplot2 

%description
Fast, flexible and user-friendly tools for distribution comparison through
direct density ratio estimation. The estimated density ratio can be used
for covariate shift adjustment, outlier-detection, change-point detection,
classification and evaluation of synthetic data quality. The package
implements multiple non-parametric estimation techniques (unconstrained
least-squares importance fitting, ulsif(), Kullback-Leibler importance
estimation procedure, kliep(), spectral density ratio estimation,
spectral(), kernel mean matching, kmm(), and least-squares
hetero-distributional subspace search, lhss()). with automatic tuning of
hyperparameters. Helper functions are available for two-sample testing and
visualizing the density ratios. For an overview on density ratio
estimation, see Sugiyama et al. (2012) <doi:10.1017/CBO9781139035613> for
a general overview, and the help files for references on the specific
estimation techniques.

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
