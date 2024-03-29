%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  hdme
%global packver   0.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.0
Release:          1%{?dist}%{?buildtag}
Summary:          High-Dimensional Regression with Measurement Error

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-glmnet >= 3.0.0
BuildRequires:    R-CRAN-ggplot2 >= 2.2.1
BuildRequires:    R-CRAN-rlang >= 1.0
BuildRequires:    R-CRAN-Rglpk >= 0.6.1
BuildRequires:    R-CRAN-Rcpp >= 0.12.15
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-glmnet >= 3.0.0
Requires:         R-CRAN-ggplot2 >= 2.2.1
Requires:         R-CRAN-rlang >= 1.0
Requires:         R-CRAN-Rglpk >= 0.6.1
Requires:         R-CRAN-Rcpp >= 0.12.15
Requires:         R-CRAN-Rdpack 
Requires:         R-stats 

%description
Penalized regression for generalized linear models for measurement error
problems (aka. errors-in-variables). The package contains a version of the
lasso (L1-penalization) which corrects for measurement error (Sorensen et
al. (2015) <doi:10.5705/ss.2013.180>). It also contains an implementation
of the Generalized Matrix Uncertainty Selector, which is a version the
(Generalized) Dantzig Selector for the case of measurement error (Sorensen
et al. (2018) <doi:10.1080/10618600.2018.1425626>).

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
