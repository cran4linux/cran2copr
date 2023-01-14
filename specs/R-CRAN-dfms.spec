%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dfms
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          1%{?dist}%{?buildtag}
Summary:          Dynamic Factor Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-collapse >= 1.8.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.1
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-collapse >= 1.8.0
Requires:         R-CRAN-Rcpp >= 1.0.1

%description
Efficient estimation of Dynamic Factor Models using the Expectation
Maximization (EM) algorithm or Two-Step (2S) estimation, supporting
datasets with missing data. The estimation options follow advances in the
econometric literature: either running the Kalman Filter and Smoother once
with initial values from PCA - 2S estimation as in Doz, Giannone and
Reichlin (2011) <doi:10.1016/j.jeconom.2011.02.012> - or via iterated
Kalman Filtering and Smoothing until EM convergence - following Doz,
Giannone and Reichlin (2012) <doi:10.1162/REST_a_00225> - or using the
adapted EM algorithm of Banbura and Modugno (2014) <doi:10.1002/jae.2306>,
allowing arbitrary patterns of missing data. The implementation makes
heavy use of the 'Armadillo' 'C++' library and the 'collapse' package,
providing for particularly speedy estimation. A comprehensive set of
methods supports interpretation and visualization of the model as well as
forecasting. Information criteria to choose the number of factors are also
provided - following Bai and Ng (2002) <doi:10.1111/1468-0262.00273>.

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
