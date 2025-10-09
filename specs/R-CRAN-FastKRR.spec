%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  FastKRR
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Kernel Ridge Regression using 'RcppArmadillo'

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-CVST 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-parsnip 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-CVST 
Requires:         R-CRAN-generics 
Requires:         R-CRAN-parsnip 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tibble 

%description
Provides core computational operations in C++ via 'RcppArmadillo',
enabling faster performance than pure R, improved numerical stability, and
parallel execution with OpenMP where available. On systems without OpenMP
support, the package automatically falls back to single-threaded execution
with no user configuration required. For efficient model selection, it
integrates with 'CVST' to provide sequential-testing cross-validation that
identifies competitive hyperparameters without exhaustive grid search. The
package offers a unified interface for exact kernel ridge regression and
three scalable approximations—Nyström, Pivoted Cholesky, and Random
Fourier Features—allowing analyses with substantially larger sample sizes
than are feasible with exact KRR. It also integrates with the 'tidymodels'
ecosystem via the 'parsnip' model specification 'krr_reg', and the S3
method tunable.krr_reg(). To understand the theoretical background, one
can refer to Wainwright (2019) <doi:10.1017/9781108627771>.

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
