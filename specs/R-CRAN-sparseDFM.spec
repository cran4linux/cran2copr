%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sparseDFM
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Estimate Dynamic Factor Models with Sparse Loadings

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.9
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 1.0.9
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-ggplot2 

%description
Implementation of various estimation methods for dynamic factor models
(DFMs) including principal components analysis (PCA) Stock and Watson
(2002) <doi:10.1198/016214502388618960>, 2Stage Giannone et al. (2008)
<doi:10.1016/j.jmoneco.2008.05.010>, expectation-maximisation (EM) Banbura
and Modugno (2014) <doi:10.1002/jae.2306>, and the novel EM-sparse
approach for sparse DFMs Mosley et al. (2023) <arXiv:2303.11892>. Options
to use classic multivariate Kalman filter and smoother (KFS) equations
from Shumway and Stoffer (1982) <doi:10.1111/j.1467-9892.1982.tb00349.x>
or fast univariate KFS equations from Koopman and Durbin (2000)
<doi:10.1111/1467-9892.00186>, and options for independent and identically
distributed (IID) white noise or auto-regressive (AR(1)) idiosyncratic
errors. Algorithms coded in 'C++' and linked to R via 'RcppArmadillo'.

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
