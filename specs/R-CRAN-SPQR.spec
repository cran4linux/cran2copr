%global __brp_check_rpaths %{nil}
%global packname  SPQR
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Semi-Parametric Quantile Regression

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildRequires:    R-CRAN-Rcpp >= 1.0.8
BuildRequires:    R-CRAN-coro >= 1.0.2
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-torch 
BuildRequires:    R-CRAN-splines2 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-loo 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-progressr 
BuildRequires:    R-CRAN-interp 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-yaImpute 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 1.0.8
Requires:         R-CRAN-coro >= 1.0.2
Requires:         R-stats 
Requires:         R-CRAN-torch 
Requires:         R-CRAN-splines2 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-loo 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-progressr 
Requires:         R-CRAN-interp 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-yaImpute 

%description
Methods for flexible estimation of conditional density and quantile
function, as well as model agnostic tools for analyzing quantile covariate
effect and variable importance. The estimation method implements the
semi-parametric quantile regression model described in Xu and Reich (2021)
<doi:10.1111/biom.13576>, and the model agnostic tools extend accumulative
local effects (ALE) to quantile regression setting.

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
