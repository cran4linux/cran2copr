%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  spFFBS
%global packver   0.0-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Spatiotemporal Propagation for Multivariate Bayesian Dynamic Learning

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 1.1.1
BuildRequires:    R-CRAN-spBPS 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-tictoc 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 1.1.1
Requires:         R-CRAN-spBPS 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-tictoc 
Requires:         R-CRAN-abind 

%description
Implementation of the Forward Filtering Backward Sampling (FFBS) algorithm
with Dynamic Bayesian Predictive Stacking (DYNBPS) integration for
multivariate spatiotemporal models, as introduced in "Adaptive Markovian
Spatiotemporal Transfer Learning in Multivariate Bayesian Modeling"
(Presicce and Banerjee, 2026+) <doi:10.48550/arXiv.2602.08544>. This
methodology enables efficient Bayesian multivariate spatiotemporal
modeling, utilizing dynamic predictive stacking to improve inference
across multivariate time series of spatial datasets. The core functions
leverage 'C++' for high-performance computation, making the framework
well-suited for large-scale spatiotemporal data analysis in parallel
computing environments.

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
