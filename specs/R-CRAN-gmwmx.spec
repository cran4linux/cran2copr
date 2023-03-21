%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gmwmx
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Estimate Functional and Stochastic Parameters of Linear Models with Correlated Residuals

License:          AGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-wv 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-longmemo 
BuildRequires:    R-CRAN-rjson 
BuildRequires:    R-CRAN-ltsa 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-wv 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-longmemo 
Requires:         R-CRAN-rjson 
Requires:         R-CRAN-ltsa 

%description
Implements the Generalized Method of Wavelet Moments with Exogenous Inputs
estimator (GMWMX) presented in Cucci, D. A., Voirol, L., Kermarrec, G.,
Montillet, J. P., and Guerrier, S. (2023)
<doi:10.1007/s00190-023-01702-8>. The GMWMX estimator allows to estimate
functional and stochastic parameters of linear models with correlated
residuals. The 'gmwmx' package provides functions to estimate, compare and
analyze models, utilities to load and work with Global Navigation
Satellite System (GNSS) data as well as methods to compare results with
the Maximum Likelihood Estimator (MLE) implemented in Hector.

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
