%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pense
%global packver   2.5.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.5.2
Release:          1%{?dist}%{?buildtag}
Summary:          Penalized Elastic Net S/MM-Estimator of Regression

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-RcppArmadillo >= 0.9.600
BuildRequires:    R-CRAN-rlang >= 0.4.0
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-testthat 
Requires:         R-CRAN-rlang >= 0.4.0
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-Rcpp 
Requires:         R-methods 
Requires:         R-parallel 

%description
Robust penalized (adaptive) elastic net S and M estimators for linear
regression. The adaptive methods are proposed in Kepplinger, D. (2023)
<doi:10.1016/j.csda.2023.107730> and the non-adaptive methods in Cohen
Freue, G. V., Kepplinger, D., Salibián-Barrera, M., and Smucler, E. (2019)
<doi:10.1214/19-AOAS1269>. The package implements robust hyper-parameter
selection with robust information sharing cross-validation according to
Kepplinger & Wei (2025) <doi:10.1080/00401706.2025.2540970>.

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
