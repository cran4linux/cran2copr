%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  aftPenCDA
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Penalized AFT Estimation via Coordinate Descent

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp 
Requires:         R-stats 

%description
Provides penalized accelerated failure time (AFT) model estimation for
right-censored and partly interval-censored survival data using induced
smoothing and coordinate descent algorithms. Supported penalties include
broken adaptive ridge (BAR), LASSO, adaptive LASSO, and SCAD. Core
estimation routines are implemented in 'C++' via 'Rcpp' and
'RcppArmadillo' for computational efficiency. The methodology is related
to Zeng and Lin (2008) <doi:10.1093/biostatistics/kxm034>, Xu et al.
(2010) <doi:10.1002/sim.2576>, Dai et al. (2018)
<doi:10.1016/j.jmva.2018.08.007>, and Choi et al. (2025)
<doi:10.48550/arXiv.2503.11268>.

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
