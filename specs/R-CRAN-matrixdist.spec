%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  matrixdist
%global packver   1.1.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.7
Release:          1%{?dist}%{?buildtag}
Summary:          Statistics for Matrix Distributions

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-nnet 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp 
Requires:         R-methods 
Requires:         R-CRAN-nnet 
Requires:         R-CRAN-reshape2 

%description
Tools for phase-type distributions including the following variants:
continuous, discrete, multivariate, in-homogeneous, right-censored, and
regression. Methods for functional evaluation, simulation and estimation
using the expectation-maximization (EM) algorithm are provided for all
models. The methods of this package are based on the following references.
Asmussen, S., Nerman, O., & Olsson, M. (1996). Fitting phase-type
distributions via the EM algorithm, Olsson, M. (1996). Estimation of
phase-type distributions from censored data, Albrecher, H., & Bladt, M.
(2019) <doi:10.1017/jpr.2019.60>, Albrecher, H., Bladt, M., & Yslas, J.
(2022) <doi:10.1111/sjos.12505>, Albrecher, H., Bladt, M., Bladt, M., &
Yslas, J. (2022) <doi:10.1016/j.insmatheco.2022.08.001>, Bladt, M., &
Yslas, J. (2022) <doi:10.1080/03461238.2022.2097019>, Bladt, M. (2022)
<doi:10.1017/asb.2021.40>, Bladt, M. (2023)
<doi:10.1080/10920277.2023.2167833>, Albrecher, H., Bladt, M., & Mueller,
A. (2023) <doi:10.1515/demo-2022-0153>, Bladt, M. & Yslas, J. (2023)
<doi:10.1016/j.insmatheco.2023.02.008>.

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
