%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  adelie
%global packver   1.0.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.8
Release:          1%{?dist}%{?buildtag}
Summary:          Group Lasso and Elastic Net Solver for Generalized Linear Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-r2r 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-r2r 
Requires:         R-CRAN-Rcpp 
Requires:         R-methods 
Requires:         R-CRAN-stringr 
Requires:         R-utils 

%description
Extremely efficient procedures for fitting the entire group lasso and
group elastic net regularization path for GLMs, multinomial, the Cox model
and multi-task Gaussian models. Similar to the R package 'glmnet' in scope
of models, and in computational speed.  This package provides R bindings
to the C++ code underlying the corresponding Python package 'adelie'.
These bindings offer a general purpose group elastic net solver, a wide
range of matrix classes that can exploit special structure to allow
large-scale inputs, and an assortment of generalized linear model classes
for fitting various types of data. The package is an implementation of
Yang, J. and Hastie, T. (2024) <doi:10.48550/arXiv.2405.08631>.

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
