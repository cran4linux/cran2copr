%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  lassoinf
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Selective Inference for the Randomized Lasso

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-methods 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-Rcpp 
Requires:         R-stats 

%description
Confidence intervals and p-values for parameters chosen by the
(randomized) lasso, valid after selection. Implements the polyhedral
approach of Lee, Sun, Sun and Taylor (2016) <doi:10.1214/15-AOS1371>, the
randomized response of Tian and Taylor (2018) <doi:10.1214/17-AOS1564> and
the exact randomized inference of Panigrahi, Fry and Taylor (2024)
<doi:10.1093/biomet/asae019>, with the truncated bivariate normal
computations of Liu (2023) <doi:10.48550/arXiv.2308.10346>. Includes
inference for user-specified estimands, screening of inactive variables
and problems fitted by 'glmnet'. Computations use a 'C++' backend with
matrix-free linear operators for wide designs.

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
