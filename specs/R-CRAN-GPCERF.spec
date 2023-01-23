%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  GPCERF
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Gaussian Processes for Estimating Causal Exposure Response Curves

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-xgboost 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-spatstat.geom 
BuildRequires:    R-CRAN-logger 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-Rfast 
BuildRequires:    R-CRAN-SuperLearner 
Requires:         R-parallel 
Requires:         R-CRAN-xgboost 
Requires:         R-stats 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-spatstat.geom 
Requires:         R-CRAN-logger 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-RcppArmadillo 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-Rfast 
Requires:         R-CRAN-SuperLearner 

%description
Provides a non-parametric Bayesian framework based on Gaussian process
priors for estimating causal effects of a continuous exposure and
detecting change points in the causal exposure response curves using
observational data. Ren, B., Wu, X., Braun, D., Pillai, N., & Dominici,
F.(2021). "Bayesian modeling for exposure response curve via gaussian
processes: Causal effects of exposure to air pollution on health
outcomes." arXiv preprint <arXiv:2105.03454>.

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
