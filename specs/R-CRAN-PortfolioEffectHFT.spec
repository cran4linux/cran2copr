%global __brp_check_rpaths %{nil}
%global packname  PortfolioEffectHFT
%global packver   1.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.8
Release:          3%{?dist}%{?buildtag}
Summary:          High Frequency Portfolio Analytics by PortfolioEffect

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         java
BuildRequires:    R-devel >= 2.13.2
Requires:         R-core >= 2.13.2
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 2.2.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rJava 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-zoo 
Requires:         R-CRAN-ggplot2 >= 2.2.0
Requires:         R-methods 
Requires:         R-CRAN-rJava 
Requires:         R-grid 
Requires:         R-CRAN-zoo 

%description
R interface to PortfolioEffect cloud service for backtesting high
frequency trading (HFT) strategies, intraday portfolio analysis and
optimization. Includes auto-calibrating model pipeline for market
microstructure noise, risk factors, price jumps/outliers, tail risk
(high-order moments) and price fractality (long memory). Constructed
portfolios could use client-side market data or access HF intraday price
history for all major US Equities. See <https://www.portfolioeffect.com/>
for more information on the PortfolioEffect high frequency portfolio
analytics platform.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
