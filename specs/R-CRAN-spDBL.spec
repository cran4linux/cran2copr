%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  spDBL
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Dynamic Bayesian Learning for Spatiotemporal Mechanistic Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-matrixsampling 
BuildRequires:    R-CRAN-invgamma 
BuildRequires:    R-CRAN-deSolve 
BuildRequires:    R-CRAN-ReacTran 
BuildRequires:    R-CRAN-LaplacesDemon 
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-CRAN-mniw 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-matrixsampling 
Requires:         R-CRAN-invgamma 
Requires:         R-CRAN-deSolve 
Requires:         R-CRAN-ReacTran 
Requires:         R-CRAN-LaplacesDemon 
Requires:         R-CRAN-matrixcalc 
Requires:         R-CRAN-mniw 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-scales 

%description
Provides tools for Bayesian learning of spatiotemporal dynamical
mechanistic models. Includes methods for parameter estimation, simulation,
and inference using hierarchical and state-space modeling approaches,
following Banerjee, Chen, Frankenburg and Zhou (2025)
<https://jmlr.org/papers/v26/22-0896.html>.

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
