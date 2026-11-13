%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ZTRecur
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Analysis for Zero-Truncated Recurrent Event Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildRequires:    R-CRAN-Rcpp >= 1.0.0
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 1.0.0
Requires:         R-CRAN-dplyr 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-stats 

%description
Provides nonparametric and Cox-type regression methods for analyzing
zero-truncated recurrent event data with supplementary information. Key
features include estimating rate and mean functions under nonparametric
marginal models; estimating time-constant regression coefficients under
standard and stratified Andersen-Gill (AG) models; and estimating
time-varying covariate effects under stratified and nonstratified Cox-type
models. Standard errors (SEs) are estimated using sandwich-based variance
estimators for nonstratified models and resampling-based procedures for
stratified models. For further details, see Chen, Hu, and Rosychuk (2026)
<doi:10.1214/25-AOAS2130>, Chen et al. (2026) <doi:10.1002/cjs.70064>, and
Chen, Hu, and Rosychuk (2026) <doi:10.48550/arXiv.2607.26210>.

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
