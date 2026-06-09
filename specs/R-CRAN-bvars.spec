%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bvars
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Forecasting with Large Vector Autoregressions

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.14
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-bsvars 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-RcppProgress 
BuildRequires:    R-CRAN-RcppTN 
BuildRequires:    R-CRAN-R6 
Requires:         R-CRAN-Rcpp >= 1.0.14
Requires:         R-CRAN-RcppArmadillo 
Requires:         R-CRAN-bsvars 
Requires:         R-CRAN-generics 
Requires:         R-CRAN-RcppProgress 
Requires:         R-CRAN-RcppTN 
Requires:         R-CRAN-R6 

%description
Provides fast and efficient procedures for Bayesian estimation and
forecasting using state-of-the-art Vector Autoregressions. This package
includes the model proposed by Chan (2020)
<doi:10.1080/07350015.2018.1451336>, that is, a Bayesian Vector
Autoregression with Minnesota priors and a flexible structure of the error
term specification. The latter includes: conditional multivariate normal
or Student’s t distributions, as well as homoskedastic or heteroskedastic
specifications with a common volatility modelled by centred or non-centred
Stochastic Volatility. Additionally, the package facilitates predictive
analyses using density forecasting and forecast-error variance
decompositions. All this is complemented by simple workflows, useful plots
and summary functions, and comprehensive documentation. The 'bvars'
package aligns with R packages 'bsvars' by Woźniak (2024)
<doi:10.32614/CRAN.package.bsvars>, 'bsvarSIGNs' by Wang & Woźniak (2025)
<doi:10.32614/CRAN.package.bsvarSIGNs>, and 'bpvars' by Woźniak (2025)
<doi:10.32614/CRAN.package.bpvars> regarding objects, workflows, and code
structure, and they constitute an integrated toolset.

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
