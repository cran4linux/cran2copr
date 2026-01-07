%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  FluxPoint
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Change Point Detection for Non-Stationary and Cross-Correlated Time Series

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-blockmatrix 
BuildRequires:    R-CRAN-corpcor 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-nnls 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-SimDesign 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-blockmatrix 
Requires:         R-CRAN-corpcor 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-nnls 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-SimDesign 

%description
Implements methods for multiple change point detection in multivariate
time series with non-stationary dynamics and cross-correlations. The
methodology is based on a model in which each component has a fluctuating
mean represented by a random walk with occasional abrupt shifts, combined
with a stationary vector autoregressive structure to capture temporal and
cross-sectional dependence. The framework is broadly applicable to
correlated multivariate sequences in which large, sudden shifts occur in
all or subsets of components and are the primary targets of interest,
whereas small, smooth fluctuations are not. Although random walks are used
as a modeling device, they provide a flexible approximation for a wide
class of slowly varying or locally smooth dynamics, enabling robust
performance beyond the strict random walk setting.

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
