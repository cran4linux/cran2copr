%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  STARRS
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Stochastic Robust Multivariate Statistics

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.13
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-CRAN-LaplacesDemon 
BuildRequires:    R-CRAN-genieclust 
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-CRAN-RSpectra 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-DescTools 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-doFuture 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-capushe 
BuildRequires:    R-CRAN-bookdown 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 1.0.13
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-mclust 
Requires:         R-CRAN-LaplacesDemon 
Requires:         R-CRAN-genieclust 
Requires:         R-CRAN-robustbase 
Requires:         R-CRAN-RSpectra 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-DescTools 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-doFuture 
Requires:         R-CRAN-future 
Requires:         R-parallel 
Requires:         R-CRAN-capushe 
Requires:         R-CRAN-bookdown 
Requires:         R-CRAN-knitr 

%description
Algorithms for robust multivariate statistics (STochAstic Robust
multivaRiate Statistics) including geometric median and geometric median
covariance computation, k-medians clustering and robust median Principal
Compenents Analysis (PCA), robust estimation of parameters for Gaussian,
Student, or Laplace mixture models. 'STARRS' provides an independent,
clean, consolidated and cohesive framework, while drawing inspiration from
the approaches implemented in packages 'Gmedian', 'Kmedians', 'RGMM',
'RobRegression'. Methods used in the package refer to H. Robbins, S. Monro
(1951) <doi:10.1214/aoms/1177729586>; D. Kraus, V. M. Panaretos (2012)
<doi:10.1093/biomet/ass037>; H. Cardot, A. Godichon-Baggioni (2015)
<doi:10.48550/arXiv.1504.02852>; A. Godichon-Baggioni, S. Robin (2024)
<doi:10.1007/s11222-023-10362-9>.

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
