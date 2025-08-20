%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gmwmx2
%global packver   0.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Estimate Functional and Stochastic Parameters of Linear Models with Correlated Residuals and Missing Data

License:          AGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-wv 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-httr2 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-wv 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-httr2 
Requires:         R-CRAN-rlang 

%description
Implements the Generalized Method of Wavelet Moments with Exogenous Inputs
estimator (GMWMX) presented in Voirol, L., Xu, H., Zhang, Y., Insolia, L.,
Molinari, R. and Guerrier, S. (2024) <doi:10.48550/arXiv.2409.05160>. The
GMWMX estimator allows to estimate functional and stochastic parameters of
linear models with correlated residuals in presence of missing data. The
'gmwmx2' package provides functions to load and plot Global Navigation
Satellite System (GNSS) data from the Nevada Geodetic Laboratory and
functions to estimate linear model model with correlated residuals in
presence of missing data.

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
