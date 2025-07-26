%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  VARtests
%global packver   2.0.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.7
Release:          1%{?dist}%{?buildtag}
Summary:          Bootstrap Tests for Cointegration and Autocorrelation in VARs

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildRequires:    R-CRAN-Rcpp >= 0.12.10
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-sn 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-methods 
Requires:         R-CRAN-Rcpp >= 0.12.10
Requires:         R-CRAN-sn 

%description
Implements wild bootstrap tests for autocorrelation in Vector
Autoregressive (VAR) models based on Ahlgren and Catani (2016)
<doi:10.1007/s00362-016-0744-0>, a combined Lagrange Multiplier (LM) test
for Autoregressive Conditional Heteroskedasticity (ARCH) in VAR models
from Catani and Ahlgren (2016) <doi:10.1016/j.ecosta.2016.10.006>, and
bootstrap-based methods for determining the cointegration rank from
Cavaliere, Rahbek, and Taylor (2012) <doi:10.3982/ECTA9099> and Cavaliere,
Rahbek, and Taylor (2014) <doi:10.1080/07474938.2013.825175>.

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
