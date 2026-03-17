%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  qshap
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Fast Calculation of Feature Contributions in Boosting Trees

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-xgboost >= 3.1.3.1
BuildRequires:    R-CRAN-Rcpp >= 1.0.14
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-lightgbm 
BuildRequires:    R-CRAN-viridisLite 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-xgboost >= 3.1.3.1
Requires:         R-CRAN-Rcpp >= 1.0.14
Requires:         R-parallel 
Requires:         R-CRAN-lightgbm 
Requires:         R-CRAN-viridisLite 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-jsonlite 
Requires:         R-methods 
Requires:         R-CRAN-progress 

%description
Computes feature-specific R-squared (R2) contributions for boosting tree
models using a Shapley-value-based decomposition of the total R-squared in
polynomial time. Supports models fitted with 'XGBoost' and 'LightGBM', and
provides efficient parallel implementations suitable for large-scale
problems. Multiple visualization tools are included for interpreting and
communicating feature contributions. The methodology is described in
Jiang, Zhang, and Zhang (2025) <doi:10.48550/arXiv.2407.03515>.

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
