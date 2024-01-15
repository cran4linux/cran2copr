%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BEKKs
%global packver   1.4.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.4
Release:          1%{?dist}%{?buildtag}
Summary:          Multivariate Conditional Volatility Modelling and Forecasting

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-mathjaxr 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-ggfortify 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-CRAN-GAS 
BuildRequires:    R-CRAN-ks 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-moments 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-mathjaxr 
Requires:         R-CRAN-gridExtra 
Requires:         R-grid 
Requires:         R-CRAN-ggfortify 
Requires:         R-parallel 
Requires:         R-CRAN-xts 
Requires:         R-stats 
Requires:         R-CRAN-future 
Requires:         R-CRAN-future.apply 
Requires:         R-CRAN-GAS 
Requires:         R-CRAN-ks 
Requires:         R-CRAN-lubridate 
Requires:         R-utils 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-moments 

%description
Methods and tools for estimating, simulating and forecasting of so-called
BEKK-models (named after Baba, Engle, Kraft and Kroner) based on the fast
Berndt–Hall–Hall–Hausman (BHHH) algorithm described in Hafner and Herwartz
(2008) <doi:10.1007/s00184-007-0130-y>.

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
