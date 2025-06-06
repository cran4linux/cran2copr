%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SharpeR
%global packver   1.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Statistical Significance of the Sharpe Ratio

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-epsiwal 
BuildRequires:    R-methods 
Requires:         R-CRAN-matrixcalc 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-epsiwal 
Requires:         R-methods 

%description
A collection of tools for analyzing significance of assets, funds, and
trading strategies, based on the Sharpe ratio and overfit of the same.
Provides density, distribution, quantile and random generation of the
Sharpe ratio distribution based on normal returns, as well as the optimal
Sharpe ratio over multiple assets. Computes confidence intervals on the
Sharpe and provides a test of equality of Sharpe ratios based on the Delta
method. The statistical foundations of the Sharpe can be found in the
author's Short Sharpe Course <doi:10.2139/ssrn.3036276>.

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
