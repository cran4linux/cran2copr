%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  facmodCS
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Cross-Section Factor Models

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-PerformanceAnalytics 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-sn 
BuildRequires:    R-CRAN-tseries 
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-CRAN-RobStatTM 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-xts 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-PerformanceAnalytics 
Requires:         R-CRAN-lattice 
Requires:         R-methods 
Requires:         R-CRAN-sn 
Requires:         R-CRAN-tseries 
Requires:         R-CRAN-robustbase 
Requires:         R-CRAN-RobStatTM 

%description
Linear cross-section factor model fitting with least-squares and robust
fitting the 'lmrobdetMM()' function from 'RobStatTM'; related volatility,
Value at Risk and Expected Shortfall risk and performance attribution
(factor-contributed vs idiosyncratic returns); tabular displays of risk
and performance reports; factor model Monte Carlo. The package authors
would like to thank Chicago Research on Security Prices,LLC for the
cross-section of about 300 CRSP stocks data (in the data.table object
'stocksCRSP', and S&P GLOBAL MARKET INTELLIGENCE for contributing 14
factor scores (a.k.a "alpha factors".and "factor exposures") fundamental
data on the 300 companies in the data.table object 'factorSPGMI'.  The
'stocksCRSP' and 'factorsSPGMI' data are not covered by the GPL-2 license,
are not provided as open source of any kind, and they are not to be
redistributed in any form.

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
