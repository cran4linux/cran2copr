%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  portvine
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Vine Based (Un)Conditional Portfolio Risk Measure Estimation

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-Rcpp >= 0.12.12
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-dtplyr 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-ppcor 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-rugarch 
BuildRequires:    R-CRAN-rvinecopulib 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-BH 
BuildRequires:    R-CRAN-kde1d 
BuildRequires:    R-CRAN-RcppEigen 
BuildRequires:    R-CRAN-RcppThread 
BuildRequires:    R-CRAN-wdm 
Requires:         R-CRAN-Rcpp >= 0.12.12
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-dtplyr 
Requires:         R-CRAN-future.apply 
Requires:         R-methods 
Requires:         R-CRAN-ppcor 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-rugarch 
Requires:         R-CRAN-rvinecopulib 
Requires:         R-CRAN-tidyr 

%description
Following Sommer (2022) <https://mediatum.ub.tum.de/1658240> portfolio
level risk estimates (e.g. Value at Risk, Expected Shortfall) are
estimated by modeling each asset univariately by an ARMA-GARCH model and
then their cross dependence via a Vine Copula model in a rolling window
fashion. One can even condition on variables/time series at certain
quantile levels to stress test the risk measure estimates.

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
