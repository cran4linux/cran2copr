%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  geeVerse
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          A Comprehensive Analysis of High Dimensional Longitudinal Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.10.2
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-Rcpp >= 0.10.2
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-quantreg 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 

%description
To provide a comprehensive analysis of high dimensional longitudinal
data,this package provides analysis for any combination of 1) simultaneous
variable selection and estimation, 2) mean regression or quantile
regression for heterogeneous data, 3) cross-sectional or longitudinal
data, 4) balanced or imbalanced data, 5) moderate, high or even ultra-high
dimensional data, via computationally efficient implementations of
penalized generalized estimating equations.

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
