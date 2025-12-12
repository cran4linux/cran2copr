%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bpvars
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Forecasting with Bayesian Panel Vector Autoregressions

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-bsvars >= 3.2
BuildRequires:    R-CRAN-Rcpp >= 1.0.12
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-RcppProgress 
BuildRequires:    R-CRAN-RcppTN 
BuildRequires:    R-CRAN-tmvtnsim 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-bsvars >= 3.2
Requires:         R-CRAN-Rcpp >= 1.0.12
Requires:         R-CRAN-R6 
Requires:         R-CRAN-RcppProgress 
Requires:         R-CRAN-RcppTN 
Requires:         R-CRAN-tmvtnsim 
Requires:         R-CRAN-generics 

%description
Provides Bayesian estimation and forecasting of dynamic panel data using
Bayesian Panel Vector Autoregressions with hierarchical prior
distributions. The models include country-specific VARs that share a
global prior distribution that extend the model by Jarociński (2010)
<doi:10.1002/jae.1082>. Under this prior expected value, each country's
system follows a global VAR with country-invariant parameters. Further
flexibility is provided by the hierarchical prior structure that retains
the Minnesota prior interpretation for the global VAR and features
estimated prior covariance matrices, shrinkage, and persistence levels.
Bayesian forecasting is developed for models including exogenous
variables, allowing conditional forecasts given the future trajectories of
some variables and restricted forecasts assuring that rates are forecasted
to stay positive and less than 100. The package implements the model
specification, estimation, and forecasting routines, facilitating coherent
workflows and reproducibility. It also includes automated
pseudo-out-of-sample forecasting and computation of forecasting
performance measures. Beautiful plots, informative summary functions, and
extensive documentation complement all this. An extraordinary
computational speed is achieved thanks to employing frontier econometric
and numerical techniques and algorithms written in 'C++'. The 'bpvars'
package is aligned regarding objects, workflows, and code structure with
the 'R' packages 'bsvars' by Woźniak (2024)
<doi:10.32614/CRAN.package.bsvars> and 'bsvarSIGNs' by Wang & Woźniak
(2025) <doi:10.32614/CRAN.package.bsvarSIGNs>, and they constitute an
integrated toolset. Copyright: 2025 International Labour Organization.

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
