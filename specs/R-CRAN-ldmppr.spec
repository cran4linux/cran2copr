%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ldmppr
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Estimate and Simulate from Location Dependent Marked Point Processes

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-parsnip >= 1.4.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.12
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-bundle 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-xgboost 
BuildRequires:    R-CRAN-ranger 
BuildRequires:    R-CRAN-dials 
BuildRequires:    R-CRAN-recipes 
BuildRequires:    R-CRAN-rsample 
BuildRequires:    R-CRAN-tune 
BuildRequires:    R-CRAN-workflows 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-hardhat 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-spatstat.geom 
BuildRequires:    R-CRAN-spatstat.explore 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-CRAN-GET 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-furrr 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-yardstick 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-parsnip >= 1.4.0
Requires:         R-CRAN-Rcpp >= 1.0.12
Requires:         R-stats 
Requires:         R-CRAN-bundle 
Requires:         R-CRAN-terra 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-xgboost 
Requires:         R-CRAN-ranger 
Requires:         R-CRAN-dials 
Requires:         R-CRAN-recipes 
Requires:         R-CRAN-rsample 
Requires:         R-CRAN-tune 
Requires:         R-CRAN-workflows 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-hardhat 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-spatstat.geom 
Requires:         R-CRAN-spatstat.explore 
Requires:         R-CRAN-nloptr 
Requires:         R-CRAN-GET 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-future 
Requires:         R-CRAN-furrr 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-yardstick 

%description
A suite of tools for estimating, assessing model fit, simulating from, and
visualizing location dependent marked point processes characterized by
regularity in the pattern. You provide a reference marked point process, a
set of raster images containing location specific covariates, and select
the estimation algorithm and type of mark model. 'ldmppr' estimates the
process and mark models and allows you to check the appropriateness of the
model using a variety of diagnostic tools. Once a satisfactory model fit
is obtained, you can simulate from the model and visualize the results.
Documentation for the package 'ldmppr' is available in the form of a
vignette.

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
