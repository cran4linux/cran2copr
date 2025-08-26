%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fect
%global packver   2.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.5
Release:          1%{?dist}%{?buildtag}
Summary:          Fixed Effects Counterfactual Estimators

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-ggplot2 >= 2.1.0
BuildRequires:    R-CRAN-foreach >= 1.4.3
BuildRequires:    R-CRAN-abind >= 1.4.0
BuildRequires:    R-CRAN-doParallel >= 1.0.10
BuildRequires:    R-CRAN-GGally >= 1.0.1
BuildRequires:    R-CRAN-Rcpp >= 0.12.3
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-fixest 
BuildRequires:    R-CRAN-doRNG 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-ggplot2 >= 2.1.0
Requires:         R-CRAN-foreach >= 1.4.3
Requires:         R-CRAN-abind >= 1.4.0
Requires:         R-CRAN-doParallel >= 1.0.10
Requires:         R-CRAN-GGally >= 1.0.1
Requires:         R-CRAN-Rcpp >= 0.12.3
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-gridExtra 
Requires:         R-grid 
Requires:         R-CRAN-fixest 
Requires:         R-CRAN-doRNG 
Requires:         R-CRAN-future 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-future.apply 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-scales 

%description
Provides tools for estimating causal effects in panel data using
counterfactual methods, as well as other modern DID estimators. It is
designed for causal panel analysis with binary treatments under the
parallel trends assumption. The package supports scenarios where
treatments can switch on and off and allows for limited carryover effects.
It includes several imputation estimators, such as Gsynth (Xu 2017),
linear factor models, and the matrix completion method. Detailed
methodology is described in Liu, Wang, and Xu (2024)
<doi:10.48550/arXiv.2107.00856> and Chiu et al. (2025)
<doi:10.48550/arXiv.2309.15983>. Optionally integrates with the
"HonestDiDFEct" package for sensitivity analyses compatible with
imputation estimators. "HonestDiDFEct" is not on CRAN but can be obtained
from <https://github.com/lzy318/HonestDiDFEct>.

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
